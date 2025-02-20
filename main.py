import requests
from PIL import Image
import numpy as np
import cv2
from io import BytesIO
from database import dbconnection
from record import PreparedRecords
from ocr import OcrTextRecognition
from utils import ImageConversion, TextConversion

def main():
    images_list = dbconnection.get_urls()
    img_conversion = ImageConversion()
    text_conversion = TextConversion()
    ocr = OcrTextRecognition()
    records = PreparedRecords()

    for id, url in images_list:

        try:
            response = requests.get(url)
        except requests.RequestException as e:
            print(f"Ошибка при получении содержимого: {e}")
        else:
            if response.status_code == 200:
                try:
                    pil_image = Image.open(BytesIO(response.content))

                    # Преобразуем изображение в массив NumPy
                    np_array = np.array(pil_image)

                    # Преобразуем массив NumPy в объект OpenCV
                    opencv_image = cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR)

                    # Предобрабатываем изображение
                    preprocessed_image = img_conversion.preprocess_image(opencv_image)

                    # Преобразуем обратно в формат RGB
                    rgb_img = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2RGB)

                    recognized_text = ocr.text_recognition(Image.fromarray(rgb_img))

                    image_text = text_conversion.post_process_text(recognized_text)
                    print(f"Текст: {id} {image_text}")

                    records.add_record(id, image_text)


                except:
                    print('exception :(')


            else:
                print(f"Не удалось загрузить изображение по адресу: {url}")

        records.clear_records_data()
        dbconnection.insert_text(records.all_records)


if __name__ == "__main__":
    main()
