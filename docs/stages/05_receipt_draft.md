# Stage 05 — ReceiptDraft

## Description
ReceiptDraft is the final output of the pipeline.
It includes status and is intended for review, not direct persistence.

## Example
```json
{
  "image_path": "sample_receipt.jpg",
  "items": [
    {
      "name": "Americano",
      "quantity": 1,
      "price": 4500
    }
  ],
  "total_candidates": [
    { "label": "TOTAL", "value": 4500 }
  ],
  "status": "OK"
}