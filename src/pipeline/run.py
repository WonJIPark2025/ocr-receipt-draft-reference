def run_pipeline(input_path: str) -> dict:
    """
    Minimal end-to-end pipeline smoke test.
    OCR engine is intentionally mocked / skipped.
    """

    # Mock OCR output
    ocr_result = {
        "text": "DUMMY OCR TEXT",
        "confidence": 0.0,
    }

    # Mock normalize / parse
    parsed = {
        "status": "AMBIGUOUS",
        "candidates": [],
    }

    return {
        "input": input_path,
        "result": parsed,
    }


if __name__ == "__main__":
    result = run_pipeline("<sample-input-path>")
    print(result)
