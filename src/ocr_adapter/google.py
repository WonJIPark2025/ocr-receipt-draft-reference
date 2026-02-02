from src.ocr.engine import OCREngine

class GoogleVisionOCREngine(OCREngine):

    def extract_text(self, image_path: str) -> dict:
        # TODO: Google Vision API 연동
        return {
            "engine": "google",
            "text": "",
            "raw": None
        }
