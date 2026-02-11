# OCR Receipt Pipeline (Reference Implementation)

This repository provides a reference implementation of an
end-to-end OCR receipt processing pipeline focused on producing
a human-reviewable draft output.

---

## Scope
- Input: Receipt images / PDFs
- OCR engine agnostic (pluggable adapter interface)
- Normalize → Preprocess → Parse → Validate → Status (OK / AMBIGUOUS / FAIL)
- Pipeline output ends at a draft stage (no persistence)

---

## Purpose
- Establish a reproducible structural baseline for OCR pipelines
- Clarify responsibility boundaries between OCR, validation, and persistence
- Serve as a reference for experimenting with OCR engines without coupling results

This repository intentionally prioritizes **structural clarity and reproducibility**
over OCR accuracy, database integration, or LLM-based enrichment.

---

## Execution Boundary
- The pipeline **does not** write to a business database
- The pipeline **does not** finalize monetary values
- The pipeline **does not** guarantee an `OK` result

The sole responsibility of the pipeline is to produce a `ReceiptDraft`
with an explicit status that downstream systems can act upon.

---

## Python Environment
- Primary compatibility target: Python 3.10.x
- Python version is not hard-pinned

## Python Compatibility
- Verified compatibility:
  - Python 3.10.x
  - Python 3.11.x

The pipeline is designed to be Python-version agnostic
within the supported range.

---

## Status
- Active reference implementation
- Intended for alignment and discussion
- Not a production-ready system

---

## Repository Structure

```text
src/
  pipeline/
    run.py        # Reference pipeline execution (ends at draft)
    draft.py      # Pipeline output → human-reviewable ReceiptDraft
  ocr/
    adapter.py         # OCR adapter interface definition
    easyocr_adapter.py # Minimal example adapter (output discarded)
docs/
  stages/
    01_input.md
    02_ocr_output.md
    03_parsed_items.md
    04_validation.md
    05_receipt_draft.md
```

---

## Contracts & Metrics

The following documents define persistence boundaries and operational monitoring:

- [Draft → DB Contract](docs/contracts/draft_to_db.md)
- [Draft Status Metrics](docs/metrics/draft_status_metrics.md)

