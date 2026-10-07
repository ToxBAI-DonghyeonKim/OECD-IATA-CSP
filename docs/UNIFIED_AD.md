

1. RDKit Cleanup → FragmentParent → Uncharger → canonical isomeric SMILES.
2. Morgan fingerprint, radius 2, 2,048 bits, for every endpoint's AD. Model-native features remain unchanged for prediction.
3. Each reference structure's density is its mean Tanimoto similarity to the five nearest **other** reference rows. Duplicate structures are retained, as in the original core24 procedure.
4. The model-specific AD threshold is the fifth percentile of those density scores.
5. A query is In domain when its maximum Tanimoto similarity to that endpoint's reference is at least the threshold; otherwise Out of domain.

The procedure is identical across models; numerical thresholds differ because each endpoint has its own reference set. No retraining or model-weight changes were made.

## Output

The same `Prediction`, `Probability`, `AD Tmax`, `AD Flag`, `AD-filtered`, `Detail`, `Summary`, and `Model manifest` sheets cover all 113 endpoints. `AD-filtered` contains PRED-0/PRED-1 for In-domain predictions and OOD otherwise. Invalid structures remain missing; OOD is not a negative call. Raw labels/probabilities are retained.

## Reference provenance

The core24 reference structures and thresholds are unchanged. DART89 references are reconstructed with the **same frozen ToxCast lineage and split procedure used for core24**: first 8,984 historical rows, 16 recorded fingerprint exclusions, endpoint nonmissing-label filtering, 80/20 split with random_state 42 and no stratification, and structure resolution from local DSSTox exports. Unresolved/invalid structures are excluded from the AD calculation and their counts are recorded. These are reconstructed references, not an independently certified copy of every original estimator's fit rows.

`ad_reference_smiles_113.json.gz`, `model_manifest_113.json`, and `dart_ad_method_audit.json` contain the executable references, thresholds and audit. `build_dart_ad.py` documents the reconstruction. The earlier raw-only limitation is resolved by adding these AD references and calculations. The previous CSP grouping itself is a separate evidence-integration layer.

ChemBAI source: https://github.com/Jiinwon/ChemBAI/tree/656171a39b6caf5e57afcaf0acdbd082c3622e70 . Its MIT notice is included in `ChemBAI_LICENSE.txt`. This package is a CSP working model collection, not a statement of OECD approval.
