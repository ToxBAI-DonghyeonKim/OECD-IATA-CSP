#!/usr/bin/env python3
"""Run the packaged 24 ToxBAI models and unified applicability-domain assessment."""

from __future__ import annotations

import argparse
import gzip
import json
import math
import sys
import warnings
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from rdkit import Chem, DataStructs, RDLogger
from rdkit.Chem import (
    AllChem,
    Crippen,
    Descriptors,
    GraphDescriptors,
    MACCSkeys,
    MolSurf,
    RDKFingerprint,
    rdFingerprintGenerator,
    rdMolDescriptors,
)
from rdkit.Chem.MolStandardize import rdMolStandardize


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "model_manifest.json"
AD_REFERENCE_PATH = ROOT / "ad_reference_smiles.json.gz"
AD_GENERATOR = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
UNCHARGER = rdMolStandardize.Uncharger()


SCALAR_DESCRIPTORS = (
    ("SlogP", Crippen.MolLogP),
    ("SMR", Crippen.MolMR),
    ("LabuteASA", rdMolDescriptors.CalcLabuteASA),
    ("TPSA", rdMolDescriptors.CalcTPSA),
    ("AMW", Descriptors.MolWt),
    ("ExactMW", Descriptors.ExactMolWt),
    ("NumLipinskiHBA", rdMolDescriptors.CalcNumLipinskiHBA),
    ("NumLipinskiHBD", rdMolDescriptors.CalcNumLipinskiHBD),
    ("NumRotatableBonds", rdMolDescriptors.CalcNumRotatableBonds),
    ("NumHBD", rdMolDescriptors.CalcNumHBD),
    ("NumHBA", rdMolDescriptors.CalcNumHBA),
    ("NumAmideBonds", rdMolDescriptors.CalcNumAmideBonds),
    ("NumHeteroAtoms", rdMolDescriptors.CalcNumHeteroatoms),
    ("NumHeavyAtoms", rdMolDescriptors.CalcNumHeavyAtoms),
    ("NumAtoms", lambda mol: mol.GetNumAtoms()),
    ("NumStereocenters", rdMolDescriptors.CalcNumAtomStereoCenters),
    ("NumUnspecifiedStereocenters", rdMolDescriptors.CalcNumUnspecifiedAtomStereoCenters),
    ("NumRings", rdMolDescriptors.CalcNumRings),
    ("NumAromaticRings", rdMolDescriptors.CalcNumAromaticRings),
    ("NumSaturatedRings", rdMolDescriptors.CalcNumSaturatedRings),
    ("NumAliphaticRings", rdMolDescriptors.CalcNumAliphaticRings),
    ("NumAromaticHeterocycles", rdMolDescriptors.CalcNumAromaticHeterocycles),
    ("NumSaturatedHeterocycles", rdMolDescriptors.CalcNumSaturatedHeterocycles),
    ("NumAliphaticHeterocycles", rdMolDescriptors.CalcNumAliphaticHeterocycles),
    ("NumAromaticCarbocycles", rdMolDescriptors.CalcNumAromaticCarbocycles),
    ("NumSaturatedCarbocycles", rdMolDescriptors.CalcNumSaturatedCarbocycles),
    ("NumAliphaticCarbocycles", rdMolDescriptors.CalcNumAliphaticCarbocycles),
    ("FractionCSP3", rdMolDescriptors.CalcFractionCSP3),
    ("Chi0v", GraphDescriptors.Chi0v),
    ("Chi1v", GraphDescriptors.Chi1v),
    ("Chi2v", GraphDescriptors.Chi2v),
    ("Chi3v", GraphDescriptors.Chi3v),
    ("Chi4v", GraphDescriptors.Chi4v),
    ("Chi1n", GraphDescriptors.Chi1n),
    ("Chi2n", GraphDescriptors.Chi2n),
    ("Chi3n", GraphDescriptors.Chi3n),
    ("Chi4n", GraphDescriptors.Chi4n),
    ("HallKierAlpha", GraphDescriptors.HallKierAlpha),
    ("Kappa1", GraphDescriptors.Kappa1),
    ("Kappa2", GraphDescriptors.Kappa2),
    ("Kappa3", GraphDescriptors.Kappa3),
)


def install_sklearn_compatibility_shim() -> None:
    """Allow legacy sklearn 1.5 GBT artifacts to load in newer sklearn releases."""
    try:
        import sklearn._loss._loss as cy_loss

        def _compat_unpickle_half_binomial(loss_type, checksum, state):
            return loss_type()

        if not hasattr(cy_loss, "__pyx_unpickle_CyHalfBinomialLoss"):
            cy_loss.__pyx_unpickle_CyHalfBinomialLoss = _compat_unpickle_half_binomial
        sys.modules.setdefault("_loss", cy_loss)
    except Exception:
        pass


def standardize_smiles(value: str) -> tuple[str | None, Chem.Mol | None, str | None]:
    text = str(value or "").strip()
    if not text:
        return None, None, "Empty SMILES"
    try:
        mol = Chem.MolFromSmiles(text)
        if mol is None:
            return None, None, "Invalid SMILES"
        mol = rdMolStandardize.Cleanup(mol)
        mol = rdMolStandardize.FragmentParent(mol)
        mol = UNCHARGER.uncharge(mol)
        Chem.SanitizeMol(mol)
        canonical = Chem.MolToSmiles(mol, canonical=True, isomericSmiles=True)
        return canonical, Chem.MolFromSmiles(canonical), None
    except Exception as exc:
        return None, None, f"Standardization failed: {exc}"


def bitvect_to_array(bitvect) -> np.ndarray:
    array = np.zeros(bitvect.GetNumBits(), dtype=np.uint8)
    DataStructs.ConvertToNumpyArray(bitvect, array)
    return array


def native_fingerprint(mol: Chem.Mol, fingerprint: str, size: int | None = None):
    if fingerprint == "MACCS":
        return MACCSkeys.GenMACCSKeys(mol)
    if fingerprint == "Morgan":
        return rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=size or 1024).GetFingerprint(mol)
    if fingerprint == "RDKit":
        return RDKFingerprint(mol, fpSize=size or 2048)
    if fingerprint == "Layered":
        return AllChem.LayeredFingerprint(mol, fpSize=size or 2048)
    if fingerprint == "Pattern":
        return AllChem.PatternFingerprint(mol, fpSize=size or 2048)
    raise ValueError(f"Unsupported fingerprint: {fingerprint}")


def native_feature_matrix(mols: list[Chem.Mol], fingerprint: str, size: int) -> np.ndarray:
    return np.vstack([bitvect_to_array(native_fingerprint(mol, fingerprint, size)) for mol in mols])


def tg416_descriptor_array(mol: Chem.Mol) -> np.ndarray:
    values = [float(function(mol)) for _, function in SCALAR_DESCRIPTORS]
    values.extend(float(value) for value in MolSurf.SlogP_VSA_(mol))
    values.extend(float(value) for value in MolSurf.SMR_VSA_(mol))
    values.extend(float(value) for value in MolSurf.PEOE_VSA_(mol))
    values.extend(float(value) for value in rdMolDescriptors.MQNs_(mol))
    result = np.asarray(values, dtype=np.float32)
    if result.shape != (119,) or not np.isfinite(result).all():
        raise ValueError("TG416 descriptor generation failed")
    return result


def tg416_feature_matrix(mols: list[Chem.Mol]) -> np.ndarray:
    rows = []
    for mol in mols:
        fingerprint = bitvect_to_array(native_fingerprint(mol, "Layered", 2048)).astype(np.float32)
        rows.append(np.concatenate([fingerprint, tg416_descriptor_array(mol)]))
    return np.vstack(rows).astype(np.float32, copy=False)


def positive_probability(estimator, features: np.ndarray) -> np.ndarray:
    probabilities = np.asarray(estimator.predict_proba(features), dtype=float)
    classes = list(getattr(estimator, "classes_", range(probabilities.shape[1])))
    try:
        positive_index = classes.index(1)
    except ValueError:
        positive_index = probabilities.shape[1] - 1
    values = probabilities[:, positive_index]
    if not np.isfinite(values).all() or ((values < 0) | (values > 1)).any():
        raise RuntimeError("Estimator returned invalid probabilities")
    return values


def portable_tree_predict(tree: dict, features: np.ndarray) -> np.ndarray:
    left = tree["children_left"]
    right = tree["children_right"]
    split_feature = tree["feature"]
    split_threshold = tree["threshold"]
    leaf_value = tree["value"]
    output = np.empty(features.shape[0], dtype=float)
    for row_index, row in enumerate(features):
        node = 0
        while left[node] != -1:
            node = left[node] if row[split_feature[node]] <= split_threshold[node] else right[node]
        output[row_index] = leaf_value[node]
    return output


def tg416_probability(model: dict, features: np.ndarray) -> np.ndarray:
    raw = np.full(features.shape[0], float(model["initial_raw_score"]), dtype=float)
    learning_rate = float(model["learning_rate"])
    for tree in model["trees"]:
        raw += learning_rate * portable_tree_predict(tree, features)
    return 1.0 / (1.0 + np.exp(-raw))


def portable_logistic_probability(model: dict, features: np.ndarray) -> np.ndarray:
    coefficient = np.asarray(model["coefficient"], dtype=float)
    intercept = float(model["intercept"])
    raw = features @ coefficient + intercept
    return 1.0 / (1.0 + np.exp(-raw))


def cached_native_features(
    cache: dict[tuple[str, int], np.ndarray],
    mols: list[Chem.Mol],
    fingerprint: str,
    size: int,
) -> np.ndarray:
    key = (fingerprint, size)
    if key not in cache:
        cache[key] = native_feature_matrix(mols, fingerprint, size)
    return cache[key]


def load_input(path: Path | None, smiles: str | None, smiles_column: str, id_column: str) -> pd.DataFrame:
    if smiles is not None:
        return pd.DataFrame([{id_column: "query_1", smiles_column: smiles}])
    if path is None:
        raise ValueError("Provide an input file or --smiles")
    suffix = path.suffix.lower()
    if suffix == ".csv":
        frame = pd.read_csv(path, dtype=str).fillna("")
    elif suffix in {".xlsx", ".xls"}:
        frame = pd.read_excel(path, dtype=str).fillna("")
    elif suffix == ".json":
        data = json.loads(path.read_text())
        if isinstance(data, list) and data and isinstance(data[0], str):
            frame = pd.DataFrame([{id_column: f"query_{i + 1}", smiles_column: value} for i, value in enumerate(data)])
        else:
            frame = pd.DataFrame(data)
    else:
        raise ValueError("Input must be CSV, XLSX, XLS, or JSON")
    if smiles_column not in frame.columns:
        raise KeyError(f"SMILES column '{smiles_column}' not found; columns={list(frame.columns)}")
    if id_column not in frame.columns:
        frame.insert(0, id_column, [f"query_{i + 1}" for i in range(len(frame))])
    return frame


def write_excel(output: Path, input_frame: pd.DataFrame, detail: pd.DataFrame, manifest: list[dict]) -> None:
    endpoint_order = [item["endpoint_code"] for item in manifest]
    base = input_frame[["query_id", "input_smiles", "standardized_smiles", "input_status"]].copy()
    tables = {}
    for value_column, prefix in (
        ("prediction_label", "Prediction"),
        ("positive_probability", "Probability"),
        ("ad_tmax", "AD Tmax"),
        ("ad_flag", "AD Flag"),
    ):
        pivot = detail.pivot(index="query_id", columns="endpoint_code", values=value_column).reindex(columns=endpoint_order)
        pivot = pivot.reset_index()
        tables[prefix] = base.merge(pivot, on="query_id", how="left")

    summary = (
        detail.groupby(["endpoint_code", "tier", "endpoint"], sort=False)
        .agg(
            queries=("query_id", "count"),
            predicted_positive=("prediction", lambda values: int(pd.Series(values).fillna(0).sum())),
            in_domain=("ad_flag", lambda values: int((values == "In domain").sum())),
            out_of_domain=("ad_flag", lambda values: int((values == "Out of domain").sum())),
            median_probability=("positive_probability", "median"),
            median_ad_tmax=("ad_tmax", "median"),
            ad_threshold=("ad_threshold", "first"),
        )
        .reset_index()
    )
    manifest_frame = pd.DataFrame(manifest)
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Summary", index=False)
        for sheet, table in tables.items():
            table.to_excel(writer, sheet_name=sheet, index=False)
        detail.to_excel(writer, sheet_name="Detail", index=False)
        manifest_frame.to_excel(writer, sheet_name="Model manifest", index=False)
        for worksheet in writer.book.worksheets:
            worksheet.freeze_panes = "A2"
            worksheet.auto_filter.ref = worksheet.dimensions
            worksheet.sheet_view.showGridLines = False
            for cell in worksheet[1]:
                cell.font = cell.font.copy(bold=True, color="FFFFFF")
                cell.fill = cell.fill.copy(fill_type="solid", fgColor="1F4E78")
            for column_cells in worksheet.columns:
                letter = column_cells[0].column_letter
                maximum = max(len(str(cell.value or "")) for cell in column_cells[: min(len(column_cells), 300)])
                worksheet.column_dimensions[letter].width = min(max(maximum + 2, 11), 45)


def main() -> None:
    parser = argparse.ArgumentParser(description="Predict 24 ToxBAI endpoints with unified AD assessment")
    parser.add_argument("input", nargs="?", type=Path, help="CSV/XLSX/JSON input file")
    parser.add_argument("-o", "--output", type=Path, default=Path("tox_bai_24model_predictions.xlsx"))
    parser.add_argument("--smiles", help="Predict one SMILES without creating an input file")
    parser.add_argument("--smiles-column", default="SMILES")
    parser.add_argument("--id-column", default="ID")
    args = parser.parse_args()

    install_sklearn_compatibility_shim()
    warnings.filterwarnings("ignore")
    RDLogger.DisableLog("rdApp.*")
    manifest = json.loads(MANIFEST_PATH.read_text())
    with gzip.open(AD_REFERENCE_PATH, "rt", encoding="utf-8") as handle:
        ad_reference = json.load(handle)

    raw = load_input(args.input, args.smiles, args.smiles_column, args.id_column)
    input_records = []
    native_mols = []
    standardized_mols = []
    valid_indices = []
    for index, row in raw.iterrows():
        input_text = str(row[args.smiles_column])
        native_mol = Chem.MolFromSmiles(input_text)
        canonical, standardized_mol, error = standardize_smiles(input_text)
        input_records.append(
            {
                "query_id": str(row[args.id_column]),
                "input_smiles": str(row[args.smiles_column]),
                "standardized_smiles": canonical or "",
                "input_status": error or "Valid",
            }
        )
        if native_mol is not None and standardized_mol is not None:
            valid_indices.append(index)
            native_mols.append(native_mol)
            standardized_mols.append(standardized_mol)
    if not standardized_mols:
        raise ValueError("No valid structures were found")

    input_frame = pd.DataFrame(input_records)
    native_cache: dict[tuple[str, int], np.ndarray] = {}
    standardized_cache: dict[tuple[str, int], np.ndarray] = {}
    ad_query_bits = [AD_GENERATOR.GetFingerprint(mol) for mol in standardized_mols]
    detail_rows = []
    model_cache = {}
    for spec in manifest:
        code = spec["endpoint_code"]
        artifact = ROOT / spec["artifact_path"]
        kind = spec["artifact_kind"]
        if kind == "tg416_portable_json":
            model = json.loads(artifact.read_text())
            features = tg416_feature_matrix(native_mols)
            probabilities = tg416_probability(model, features)
        elif kind == "portable_logistic_json":
            model = json.loads(artifact.read_text())
            feature_mols = standardized_mols if code == "T2_HERSH" else native_mols
            feature_cache = standardized_cache if code == "T2_HERSH" else native_cache
            features = cached_native_features(
                feature_cache, feature_mols, str(spec["native_fingerprint"]), int(spec["model_features"])
            )
            probabilities = portable_logistic_probability(model, features)
        elif kind == "xgboost_booster":
            import xgboost as xgb

            feature_mols = standardized_mols if code == "T2_UTERO" else native_mols
            feature_cache = standardized_cache if code == "T2_UTERO" else native_cache
            features = cached_native_features(
                feature_cache, feature_mols, str(spec["native_fingerprint"]), int(spec["model_features"])
            )
            booster = xgb.Booster()
            booster.load_model(artifact)
            matrix = xgb.DMatrix(features, feature_names=booster.feature_names)
            probabilities = np.asarray(booster.predict(matrix), dtype=float)
        elif kind == "tier2_bundle":
            bundle = joblib.load(artifact)
            fp = str(bundle["fingerprint"])
            features = cached_native_features(standardized_cache, standardized_mols, fp, int(spec["model_features"]))
            probabilities = positive_probability(bundle["model"], features)
        else:
            estimator = model_cache.setdefault(str(artifact), joblib.load(artifact))
            fp = str(spec["native_fingerprint"])
            features = cached_native_features(native_cache, native_mols, fp, int(spec["model_features"]))
            probabilities = positive_probability(estimator, features)

        decision_threshold = float(spec["decision_threshold"])
        predictions = (probabilities >= decision_threshold).astype(int)
        training_bits = [AD_GENERATOR.GetFingerprint(Chem.MolFromSmiles(value)) for value in ad_reference[code]]
        tmax_values = np.asarray(
            [max(DataStructs.BulkTanimotoSimilarity(query, training_bits)) for query in ad_query_bits],
            dtype=float,
        )
        ad_threshold = float(spec["ad_threshold"])
        for local_index, source_index in enumerate(valid_indices):
            query = input_frame.iloc[source_index]
            prediction = int(predictions[local_index])
            tmax = float(tmax_values[local_index])
            detail_rows.append(
                {
                    "query_id": query["query_id"],
                    "input_smiles": query["input_smiles"],
                    "standardized_smiles": query["standardized_smiles"],
                    "endpoint_code": code,
                    "tier": spec["tier"],
                    "endpoint": spec["endpoint"],
                    "prediction": prediction,
                    "prediction_label": f"PRED-{prediction}",
                    "positive_probability": float(probabilities[local_index]),
                    "decision_threshold": decision_threshold,
                    "ad_tmax": tmax,
                    "ad_threshold": ad_threshold,
                    "ad_margin": tmax - ad_threshold,
                    "ad_flag": "In domain" if tmax >= ad_threshold else "Out of domain",
                }
            )

    detail = pd.DataFrame(detail_rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() == ".csv":
        detail.to_csv(args.output, index=False, encoding="utf-8-sig")
    elif args.output.suffix.lower() == ".json":
        args.output.write_text(json.dumps(detail.to_dict(orient="records"), ensure_ascii=False, indent=2))
    else:
        write_excel(args.output, input_frame, detail, manifest)
    print(f"Predicted {len(standardized_mols)} valid substances across {len(manifest)} endpoints")
    print(f"Wrote {args.output.resolve()}")


if __name__ == "__main__":
    main()
