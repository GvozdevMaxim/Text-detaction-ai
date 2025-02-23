import easyocr
import numpy as np


class OcrTextRecognition:
    @staticmethod
    def text_recognition(image):
        reader = easyocr.Reader(['ru', 'en'], verbose=False)
        result = reader.readtext(np.array(image))
        all_text = []
        for coords, text, confidence in result:
            if confidence >= 0.6:
                all_text.append(text)
        if all_text:
            return ' '.join(all_text)
        return None
