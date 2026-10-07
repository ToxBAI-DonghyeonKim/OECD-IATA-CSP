# Selection provenance and verification

## Conversation sources

| Conversation | Relevant decision |
|---|---|
| OECD IATA CSP 추가 모델 개발 관련 | Final Hershberger Pattern + Logistic Regression, threshold 0.01; final bundle and model card |
| Continuing from ToxBAI AD 재평가: Locate the previously genera… | Portable 24-endpoint prediction package completed 27 August 2026; common AD reevaluation |
| 0924 IATA CSP 리비전 | Tier 3 TG414/TG416/TG421 scope and distinction between ER/AR activity and DART potential |
| 0928 decision tree | Later Group 1–5 integration workflow; TG416 label interpretation |

## Historical reproduction record

The 27 August conversation recorded:
- 607 case-study chemicals.
- 3,627 observed cells retained.
- 10,941 gap-filled predictions.
- Zero class disagreements and zero AD disagreements when replaying those predictions.
- Maximum probability difference: 8.9 × 10^-7.
- AD: 10,120 In Domain, 821 Out of Domain.

These are records of the previous run. They have **not** been independently repeated in the present repository preparation.

## Current verification on 7 October 2026

- Confirmed the original package and 24 individual artifact filenames exist in the prior workspace.
- Confirmed the final Hershberger settings from the latest relevant conversation.
- Created a separate private GitHub repository.
- Recovered the original ZIP from iCloud and verified ZIP integrity.
- Verified 33 SHA256 entries: zero mismatches.
- Executed the supplied two-substance sample across all 24 endpoints: 48 endpoint predictions completed.
- Runtime: RDKit 2024.03.5, scikit-learn 1.5.2, XGBoost 2.1.1.
- Confirmed manifest T2_HERSH feature representation Pattern and threshold 0.01.
- Uploaded the unchanged original inference ZIP and its browsing documentation.

No model weights were reconstructed or retrained. Historical 607-substance reproduction metrics above were not rerun in this preparation.
