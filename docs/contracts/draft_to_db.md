# ReceiptDraft → DB Input Contract

## Purpose
This document defines the contract for converting a `ReceiptDraft`
into a database input object.

The conversion is **explicitly outside** of the OCR pipeline and
is only allowed when the draft reaches `status == OK`.

---

## Usage

This contract defines the criteria for persisting
ReceiptDraft objects into the database.

Applied in:
- src/pipeline/draft.py
- DB input validation layer

---

## Scope

### In Scope
- Field-level mapping from `ReceiptDraft` to DB input
- Validation preconditions for persistence

### Out of Scope
- OCR accuracy
- Parsing rules
- Database schema design
- Persistence logic implementation

---

## Preconditions

A `ReceiptDraft` may be converted to a DB input **only if**:

- `draft.status == "OK"`
- Required fields are present
- No ambiguity remains in totals or items

Drafts with status `AMBIGUOUS` or `FAIL` **must not** be persisted.

Persistence must be deterministic and reproducible based solely on the ReceiptDraft object.


---

## Required Fields

The following fields must be present for DB conversion:

- image_path
- at least one item
- a resolved total value

---

## ReceiptDraft (Input Example)

Example (simplified):

```json
{
  "image_path": "sample_receipt.jpg",
  "items": [
    { "name": "Americano", "quantity": 1, "price": 4500 }
  ],
  "total_candidates": [
    { "label": "TOTAL", "value": 4500 }
  ],
  "status": "OK"
}
```

## DB Input (Resolved Output Example)

The DB input must contain a resolved `total` value, not multiple `total_candidates`.

```json
{
  "image_path": "sample_receipt.jpg",
  "store_name": "Cafe A",
  "date": "2026-02-08",
  "total": 4500,
  "items": [
    { "name": "Americano", "quantity": 1, "price": 4500 }
  ]
}
```