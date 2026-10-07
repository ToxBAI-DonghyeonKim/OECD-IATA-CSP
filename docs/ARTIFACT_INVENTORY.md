# Original artifact inventory

Source package: `ToxBAI_24model_prediction_bundle_2026-08-27.zip` (recorded size: 3,659,777 bytes).

## Selected inference artifacts

| IDs | Files |
|---|---|
| ER01 | models/ER01.ubj |
| ER02 | models/ER02.joblib |
| ER03 | models/ER03.joblib |
| ER04, ER05 | models/ER04.ubj, models/ER05.ubj |
| ER06–ER11 | models/ER06.joblib through models/ER11.joblib |
| ER12 | models/ER12.ubj |
| AR01–AR04 | models/AR01.joblib through models/AR04.joblib |
| AR05 | models/AR05.ubj |
| AR06, AR07 | models/AR06.joblib, models/AR07.joblib |
| T2_HERSH | models/T2_HERSH.json |
| T2_UTERO | models/T2_UTERO.ubj |
| T3_414 | models/T3_414.joblib |
| T3_416 | models/T3_416.json |
| T3_421 | models/T3_421.json |

The JSON logistic exports and native XGBoost artifacts were created to preserve predictions while addressing serialized estimator compatibility. File extensions alone do not identify all feature settings; use the original manifest.

## Supporting files

- predict_24.py
- model_manifest.json
- method_audit.json
- ad_reference_smiles.json.gz
- input_template.csv
- requirements.txt
- environment.yml
- run_prediction.command
- SHA256SUMS.txt
- README.md

## Verification

The ZIP integrity test passed; all 33 checksum entries matched. The supplied two-substance input completed all 24 endpoints. The original manifest and method audit are also available under `reference/` for browsing.
