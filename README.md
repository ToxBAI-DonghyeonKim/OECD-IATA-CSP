# OECD IATA CSP — ToxBAI final model collection

This repository organizes the final model artifacts selected in the OECD IATA case-study work on consumer product chemicals: ER/AR activity and developmental and reproductive toxicity (DART) potential.

## Model scope

| Tier | Endpoints | Count |
|---|---|---:|
| Tier 1 | ER assays (ER01–ER12), AR assays (AR01–AR07) | 19 |
| Tier 2 | Uterotrophic agonist (T2_UTERO), Hershberger antagonist (T2_HERSH) | 2 |
| Tier 3 | TG 414, TG 416, TG 421 | 3 |
| **Total** | | **24** |

“Final” refers to the selected inference artifacts in the case-study workflow. It does not imply OECD approval.

## Download and run

[Download the complete 24-model inference package](ToxBAI_24model_prediction_bundle_2026-08-27.zip).

The ZIP includes all 24 model artifacts, inference code, AD reference structures, original manifest and checksums. Extract it before running:

```bash
unzip ToxBAI_24model_prediction_bundle_2026-08-27.zip
cd ToxBAI_24model_prediction_bundle_2026-08-27
python -m pip install -r requirements.txt
python predict_24.py input_template.csv -o predictions.xlsx
```

Prepare input with `ID` and `SMILES` columns. CSV, XLSX and JSON are supported by the original script. Output includes predicted classes, positive probabilities and endpoint-specific AD scores/flags.

For a single SMILES:

```bash
python predict_24.py --smiles "CCO" -o prediction.xlsx
```

The original model settings and weights are preserved. JSON/native XGBoost exports retain the established portable deployment formats.

## Confirmed final Hershberger selection

- Pattern fingerprint + Logistic Regression.
- C = 50; L1 penalty; liblinear solver.
- Classification threshold: **0.0100**.
- Selection criterion: maximize specificity subject to sensitivity ≥ 0.80 using 10 × 5 repeated out-of-fold predictions.
- Recorded repeated-OOF metrics: sensitivity 0.800, specificity 0.416, F1 0.528, ROC-AUC 0.699.
- The earlier proposed threshold 0.44 was not adopted as the final threshold.

These metrics are historical internal-validation results, not a new evaluation performed for this repository.

## Applicability domain

The recorded common AD procedure uses standardized Morgan fingerprints (radius 2, 2,048 bits). For each endpoint, the fifth percentile of the training chemicals' mean top-five-neighbor Tanimoto similarities defines its threshold. A query is In Domain when its maximum similarity to that endpoint's training reference is at least the threshold.

The AD decision accompanies the prediction; it does not replace or alter the predicted class. Exact structure preprocessing and endpoint thresholds must be read from the recovered inference code and manifest.

## Interpretation

The Tier 3 outputs follow their training-label definitions. They do not establish an endocrine mechanism or directly predict every endocrine-related observation. In particular, the recorded TG416 positive label is high concern defined by LEL < 1,000 mg/kg bw/day; a negative prediction does not mean absence of reproductive toxicity.

The later IATA decision tree integrates apical and mechanistic evidence. It is a separate evidence-integration layer; the 24 endpoint predictions alone are not the complete Group 1–5 classification algorithm.

## Documentation

- [Full model catalog](docs/MODEL_CATALOG.md)
- [Artifact inventory](docs/ARTIFACT_INVENTORY.md)
- [Selection provenance and verification](docs/PROVENANCE.md)

Prepared from the user's prior conversations on 7 October 2026.
