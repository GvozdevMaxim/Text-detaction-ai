import requests
from PIL import Image
import numpy as np
import cv2
from io import BytesIO
from database import dbconnection
from record import PreparedRecords
from ocr import OcrTextRecognition
from utils import TextConversion


def main():
    images_list = dbconnection.get_urls()
    # img_conversion = ImageConversion()
    text_conversion = TextConversion()
    ocr = OcrTextRecognition()
    records = PreparedRecords()

    for id, url in images_list:
        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print("Ошибка: Превышено время ожидания ответа от сервера.")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
        else:
            if response.status_code == 200:
                try:
                    pil_image = Image.open(BytesIO(response.content))

                    # Преобразуем изображение в массив NumPy
                    np_array = np.array(pil_image)

                    # Преобразуем массив NumPy в объект OpenCV
                    opencv_image = cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR)

                    # Предобрабатываем изображение
                    # preprocessed_image = img_conversion.preprocess_image(opencv_image)

                    # Преобразуем обратно в формат RGB
                    rgb_img = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

                    recognized_text = ocr.text_recognition(Image.fromarray(rgb_img))
                    if recognized_text:
                        image_text = text_conversion.post_process_text(recognized_text)
                        print(f"Текст: {id} {image_text}")

                        records.add_record(id, image_text)


                except:
                    print('Изображение по ссылке не было найдено')

            else:
                print(f"Url: {url} некорректен либо недоступен")

        if records.all_records:
            dbconnection.insert_text(records.all_records)
        records.clear_records_data()


if __name__ == "__main__":
    main()
