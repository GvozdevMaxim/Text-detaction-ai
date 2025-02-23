import re

# Попытка улучшить качество распознования текста №1
# class ImageConversion:
    # @staticmethod
    # def preprocess_image(image):
    #     # Преобразуем изображение в оттенках серого
    #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     # Применяем адаптивную биномализацию
    #     thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    #     return thresh


class TextConversion:
    @staticmethod
    def post_process_text(text):
        # Убираем лишние символы
        clean_text = re.sub(r'[^\w\s]', '', text)
        # Приведение к нижнему регистру
        clean_text = clean_text.lower()
        # Замена нескольких подряд идущих пробелов одним
        clean_text = re.sub(r'\s+', ' ', clean_text)
        return clean_text.strip()
