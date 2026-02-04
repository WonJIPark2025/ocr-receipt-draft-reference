import json
from pathlib import Path
from datetime import datetime, timezone

from src.ocr.engine import GoogleVisionOCREngine
from src.preprocessing.basic import preprocess_raw_text
from src.parsing.item_blocks import group_item_blocks
from src.parsing.items import parse_items_from_blocks
from src.parsing.totals import parse_totals
from src.validation.total_check import validate_item_sum

def save_json(data: dict, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# =========================
# 1. OCR → Item Parsing
# =========================
def run_pipeline(image_path: str) -> dict:
    image_path = Path(image_path)

    # 1. OCR
    ocr_engine = GoogleVisionOCREngine()
    raw_text = ocr_engine.extract_text(str(image_path))

    save_json(
        {
            "engine": "google_vision",
            "image_path": str(image_path),
            "raw_text": raw_text,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        Path("data/processed/ocr_raw") / f"{image_path.stem}.json"
    )

    # 2. Preprocessing
    lines = preprocess_raw_text(raw_text)

    save_json(
        {
            "image_path": str(image_path),
            "lines": lines,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        Path("data/processed/preprocessed") / f"{image_path.stem}.json"
    )

    # 3. Item Parsing
    blocks = group_item_blocks(lines)
    items = parse_items_from_blocks(blocks)

    return {
        "image_path": str(image_path),
        "raw_text": raw_text,
        "lines": lines,
        "items": items
    }


# =========================
# 2. Totals + Validation
# =========================
def run_receipt_pipeline(parsed_receipt: dict) -> dict:
    items = parsed_receipt["items"]
    raw_text = parsed_receipt["raw_text"]
    item_sum = sum(i["amount"] for i in items)

    # 1. Totals parsing (multiple candidates)
    totals = parse_totals({
        "text": raw_text,
        "item_sum": item_sum
    })

    # 2. Validation
    validation = validate_item_sum(
        items,
        totals["candidates"]
    )

    # 3. Receipt assembly
    receipt = {
        "image_path": parsed_receipt.get("image_path"),
        "items": items,
        "totals": totals,
        "validation": validation,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    # 4. Routing by validation status
    output_dir = route_receipt_by_status(receipt)

    output_path = output_dir / f"{Path(receipt['image_path']).stem}.json"

    save_json(receipt, output_path)

    print(f"[OK] Receipt saved → {output_path}")

    return receipt


# =========================
# 3. Routing
# =========================
def route_receipt_by_status(receipt: dict) -> Path:
    status = receipt["validation"]["status"].lower()

    base_dir = Path("data/processed/receipt")

    if status == "ok":
        return base_dir / "ok"
    elif status == "mismatch":
        return base_dir / "mismatch"
    elif status == "ambiguous":
        return base_dir / "ambiguous"
    elif status == "no_total":
        return base_dir / "no_total"
    else:
        # 미래 확장 대비
        return base_dir / "unknown"
