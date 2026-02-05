from src.ocr.easyocr_adapter import EasyOCREngine

if __name__ == "__main__":
    engine = EasyOCREngine()
    result = engine.run("dummy.jpg")
    print(result)
