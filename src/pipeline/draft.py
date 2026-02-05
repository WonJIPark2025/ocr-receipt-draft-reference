def to_receipt_draft(pipeline_result: dict) -> dict:
    """
    Convert pipeline output into a human-reviewable draft.
    This draft is NOT persisted directly.
    """

    return {
        "image_path": pipeline_result.get("image_path"),
        "items": pipeline_result.get("items", []),
        "total_candidates": pipeline_result
            .get("totals", {})
            .get("candidates", []),
        "validation_status": pipeline_result
            .get("validation", {})
            .get("status"),
        "notes": "Draft output. Human confirmation required."
    }
