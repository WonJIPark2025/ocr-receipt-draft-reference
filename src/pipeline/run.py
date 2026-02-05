from src.pipeline.draft import to_receipt_draft


def run_pipeline(image_path: str) -> dict:
    """
    Reference pipeline execution.

    This pipeline intentionally skips actual OCR execution and
    produces a human-reviewable draft output.
    """

    pipeline_result = {
        "image_path": image_path,
        "items": [],
        "totals": {"candidates": []},
        "validation": {"status": "AMBIGUOUS"},
    }

    return to_receipt_draft(pipeline_result)


if __name__ == "__main__":
    result = run_pipeline("<sample-input-path>")
    print(result)
