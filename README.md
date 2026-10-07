# OECD IATA CSP — 113 models with unified AD

[Download the 113-model ZIP](ToxBAI_113model_prediction_bundle.zip). [Full DART catalog](docs/DART_MODEL_CATALOG.md).

24 core endpoints + 89 General DART mechanism assays. All 113 now use the same applicability-domain procedure.

```sh
python -m pip install -r requirements.txt
python predict_113.py input_template.csv -o predictions_113.xlsx
python predict_113.py --smiles "CCO" -o ethanol_predictions.xlsx
```

## Unified applicability domain

1. RDKit Cleanup → FragmentParent → Uncharger → canonical isomeric SMILES.
2. Morgan fingerprint, radius 2, 2,048 bits, for every endpoint's AD. Model-native features remain unchanged for prediction.
3. Each reference structure's density is its mean Tanimoto similarity to the five nearest **other** reference rows. Duplicate structures are retained, as in the original core24 procedure.
4. The model-specific AD threshold is the fifth percentile of those density scores.
5. A query is In domain when its maximum Tanimoto similarity to that endpoint's reference is at least the threshold; otherwise Out of domain.

The procedure is identical across models; numerical thresholds differ because each endpoint has its own reference set. No retraining or model-weight changes were made.

## Output

The same `Prediction`, `Probability`, `AD Tmax`, `AD Flag`, `AD-filtered`, `Detail`, `Summary`, and `Model manifest` sheets cover all 113 endpoints. `AD-filtered` contains PRED-0/PRED-1 for In-domain predictions and OOD otherwise. Invalid structures remain missing; OOD is not a negative call. Raw labels/probabilities are retained.
