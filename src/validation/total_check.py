def validate_item_sum(items: list, candidates: list) -> dict:
    item_sum = sum(i["amount"] for i in items)

    if not candidates:
        return {
            "status": "NO_TOTAL",
            "item_sum": item_sum
        }

    # score 기준 정렬
    sorted_candidates = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )

    best = sorted_candidates[0]

    # 상위 후보 간 점수 차이가 작으면 ambiguous
    if len(sorted_candidates) > 1:
        if best["score"] - sorted_candidates[1]["score"] < 20:
            return {
                "status": "AMBIGUOUS",
                "item_sum": item_sum,
                "candidates": sorted_candidates[:2]
            }

    if best["value"] == item_sum:
        return {
            "status": "OK",
            "item_sum": item_sum,
            "matched_total": best
        }

    return {
        "status": "MISMATCH",
        "item_sum": item_sum,
        "candidates": sorted_candidates
    }
