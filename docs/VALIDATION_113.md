# Unified AD validation

All 113 models share the recorded core24 AD algorithm. Model artifact hashes are unchanged. Core24 reference structures and thresholds are unchanged. The previous two-query run was compared with the updated run: all 48 core and 178 DART raw predictions/probabilities were unchanged (probability tolerance 1e-12), and all core AD flags were identical. Every model has a nonempty reference set, and its first reference has self Tmax 1 and is In domain. AD-filtered labels match the AD flags. This is execution and regression verification, not external predictive-performance validation.

```json
{
  "models": 113,
  "core_predictions_unchanged": 48,
  "dart_predictions_unchanged": 178,
  "dart_references": 23892,
  "min_dart_references": 20,
  "missing_or_rejected_dart_fit_rows": 1660,
  "sample_ad_flags": {
    "In domain": 222,
    "Out of domain": 4
  }
}
```

ZIP SHA256: `8f11455e66c74532cdfbc43dce20c478497d7790f1dfa14c9098cd56a9b42193`.
