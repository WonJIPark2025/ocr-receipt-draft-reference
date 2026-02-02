import re

PRICE_PATTERN = re.compile(
    r"(?P<unit>\d{1,3}(?:,\d{3})*)\s+(?P<qty>\d+)\s+(?P<amount>\d{1,3}(?:,\d{3})*)"
)

def parse_items_from_blocks(blocks: list[list[str]]) -> list[dict]: # 라인에서 블록으로 수정
    items = []

    for block in blocks:
        name = block[0]
        text = " ".join(block)

        match = PRICE_PATTERN.search(text)
        if not match:
            continue

        items.append({
            "name": name,
            "unit_price": int(match.group("unit").replace(",", "")),
            "quantity": int(match.group("qty")),
            "amount": int(match.group("amount").replace(",", ""))
        })

    return items
