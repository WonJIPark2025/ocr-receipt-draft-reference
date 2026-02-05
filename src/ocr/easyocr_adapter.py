from .adapter import OCREngine

class EasyOCREngine(OCREngine):

    def __init__(self):
        try:
            import easyocr # optional dependency
            self.reader = easyocr.Reader(['ko', 'en'])
        except Exception:
            self.reader = None

    def run(self, image_path: str) -> dict:
        if not self.reader:
            return {"engine": "easyocr", "raw": None}

        _ = self.reader.readtext(image_path)
        return {
            "engine": "easyocr",
            "raw": None  # Intentionally discard OCR output
        }
