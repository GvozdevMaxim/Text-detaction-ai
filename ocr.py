import easyocr
import numpy as np


class OcrTextRecognition:
    @staticmethod
    def text_recognition(image):
        reader = easyocr.Reader(['ru', 'en'], verbose=False)
        result = reader.readtext(np.array(image))
        all_text = []
        for coords, text, confidence in result:
            if confidence >= 0.5:  # Оставляем только строки с высокой уверенностью
                all_text.append(text)
        return ' '.join(all_text)
