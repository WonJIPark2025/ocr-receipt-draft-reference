from src.ocr.legacy.google_engine import GoogleVisionLegacyEngine

class GoogleVisionOCREngine(GoogleVisionLegacyEngine):

    def run(self, image_path: str) -> dict:
        # TODO: Google Vision API 연동
        return {
            "engine": "google",
            "text": "",
            "raw": None
        }
