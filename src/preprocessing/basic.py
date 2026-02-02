def preprocess_raw_text(raw_text: str) -> list[str]:
    lines = raw_text.splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    return lines
