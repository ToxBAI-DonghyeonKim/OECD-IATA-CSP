# OECD IATA CSP — 113 models

[Download the 113-model ZIP](ToxBAI_113model_prediction_bundle.zip). See [89-model catalog](docs/DART_MODEL_CATALOG.md) and [24-model catalog](docs/MODEL_CATALOG.md).

24 core models + 89 General DART mechanism assay models. Core artifacts are preserved from the 2026-08-27 bundle. The 89 models are selected by AEID, assay, fingerprint and algorithm from the agreed DART AOP 89-assay list and ChemBAI's ToxCast_model(F1) directory.

```sh
python -m pip install -r requirements.txt
python predict_113.py input_template.csv -o predictions_113.xlsx
```

The core24 sheets retain their existing applicability-domain assessment. DART raw labels and probabilities are stored separately in `DART Prediction`, `DART Probability`, and `DART Detail`. **The 89 source artifacts do not supply AD reference structures/cutoffs. Their raw labels must not be presented as AD-filtered evidence or used to reproduce the final CSP grouping without the original AD data.**

`model_manifest_113.json` lists all models. `dart_model_manifest.json` records each source path, pinned commit, Git blob SHA, SHA256, feature size and listed performance. No retraining was performed. The original 24-model method audit and AD references are retained.

Source: https://github.com/Jiinwon/ChemBAI/tree/656171a39b6caf5e57afcaf0acdbd082c3622e70 . Third-party model rights remain with the original authors; no new license is asserted. This collection is a CSP working model package, not a statement of OECD approval.
