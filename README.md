# OCR Receipt Pipeline (Reference Implementation)
This repository provides a reference implementation of an
end-to-end OCR receipt processing pipeline.

## Scope
- Input: Receipt images / PDFs
- OCR engine agnostic
- Normalize → Preprocess → Parse → Status (OK / AMBIGUOUS / FAIL)

## Purpose
- Establish a reproducible baseline pipeline
- Serve as a reference for OCR engine comparison
- Not a finalized production standard

This repository intentionally prioritizes structural clarity and reproducibility
over completeness of OCR or LLM integrations.

## Python Environment
- Primary compatibility target: Python 3.10.x
- Python version is not hard-pinned pending OCR engine comparison

## Python Compatibility
- Development has been performed using a recent Python release
- Compatibility has been verified within the following range:
  - Python 3.10.x
  - Python 3.11.x

The pipeline is designed to be Python-version agnostic
within the supported range.

## Status
- Active development
- Intended to be mirrored into team repositories after agreement

## Repository Structure

```text
src/
  pipeline/
    run.py        # Reference pipeline execution (ends at draft)
    draft.py      # Pipeline output → human-reviewable draft
  ocr/
    adapter.py   # OCR adapter interface
    easyocr_adapter.py  # Minimal example adapter (output discarded)