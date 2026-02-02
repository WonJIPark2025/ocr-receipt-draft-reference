import re

TOTAL_PATTERNS = [
    ("합계", r"합\s*계\s*([0-9,]+)", 40),
    ("계", r"\b계\s*([0-9,]+)", 30),
    ("총액", r"총\s*금\s*액\s*([0-9,]+)", 20),
]

def parse_totals(parsed_receipt: dict) -> dict:
    text = parsed_receipt.get("text", "")
    item_sum = parsed_receipt.get("item_sum")

    candidates = []

    for semantic_label, pattern, base_score in TOTAL_PATTERNS:
        for m in re.finditer(pattern, text):
            value = int(m.group(1).replace(",", ""))
            score = base_score

            if item_sum is not None:
                diff = abs(item_sum - value)
                if diff == 0:
                    score += 50
                elif diff <= 100:
                    score += 20

            raw_label = m.group(0)

            candidates.append({
                "label": semantic_label,     # 의미 고정
                "raw_label": raw_label,      # OCR 원문
                "value": value,
                "score": score,
                "source": "regex"
            })
            
    return { "candidates": candidates }