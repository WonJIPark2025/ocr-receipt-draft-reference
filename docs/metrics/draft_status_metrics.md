# Draft Status Metrics

## Purpose
This document defines operational metrics for monitoring
the downstream impact of OCR and parsing without evaluating
OCR accuracy directly.

Metrics are derived exclusively from `ReceiptDraft.status`.

---

## Usage

This document defines status-based monitoring rules applied in:

- `src/pipeline/draft.py` (ReceiptDraft generation)
- Validation stage (status assignment)
- Logging layer (status telemetry recording)
- DB persistence gate (`status == OK`)

---

## Core Metrics

### Status Distribution

| Metric | Definition | Interpretation |
|------|------------|----------------|
| OK rate | OK / Total drafts | Eligible for persistence |
| AMBIGUOUS rate | AMBIGUOUS / Total drafts | Human review workload |
| FAIL rate | FAIL / Total drafts | Missing critical fields or structural corruption |

> These metrics reflect end-to-end impact (OCR → parsing → validation),
> not OCR accuracy in isolation.

---

## Monitoring Principles

- Metrics are **observational**, not prescriptive
- No metric is used to force an `OK` outcome
- Database writes are gated strictly by `status == OK`, 
and AMBIGUOUS and FAIL are excluded from persistence.
- Status metrics must not alter validation logic directly.

---

## Alerting Guidelines (Initial)

| Condition | Action |
|----------|--------|
| OK rate drops sharply | Investigate OCR input quality or parsing rules |
| AMBIGUOUS rate spikes | Review validation criteria or add review hints |
| FAIL rate increases | Inspect OCR failures or input anomalies |

Alerts trigger **investigation**, not automatic rule changes.

---

## Attribution (Non-Goals)

The following are explicitly **out of scope**:
- OCR accuracy scoring
- Per-engine performance ranking
- SLA guarantees based on OCR metrics

All analysis remains at the `ReceiptDraft` level.

---

## Telemetry Fields (Optional)

Draft-level metadata may be logged for analysis purposes only:

```json
{
  "status": "OK",
  "ocr_engine": "easyocr",
  "ocr_text_length": 812,
  "num_items": 1,
  "num_total_candidates": 1,
  "created_at": "2026-02-08T12:00:00Z"
}
```