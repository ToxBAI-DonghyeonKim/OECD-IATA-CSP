# Final endpoint catalog

Read directly from the recovered original model manifest.

| ID | Endpoint | Algorithm | Features | Class threshold | AD threshold |
|---|---|---|---|---:|---:|
| ER01 | NVS_NR_hER | xgb | Morgan (1024) | 0.5 | 0.186430 |
| ER02 | OT_ER_ERaERb_0480 | logistic | Pattern (2048) | 0.5 | 0.204822 |
| ER03 | OT_ER_ERbERb_0480 | rf | Pattern (2048) | 0.5 | 0.204822 |
| ER04 | ATG_ERE_CIS | xgb | Layered (2048) | 0.5 | 0.232018 |
| ER05 | ATG_ERa_TRANS | xgb | Layered (2048) | 0.5 | 0.232018 |
| ER06 | ATG_hERa_XSP1 | gbt | RDKit (2048) | 0.5 | 0.129326 |
| ER07 | ATG_hERb_XSP1 | dt | RDKit (2048) | 0.5 | 0.129326 |
| ER08 | ATG_hERb_XSP2 | logistic | Pattern (2048) | 0.5 | 0.147663 |
| ER09 | ATG_hERa_XSP2 | dt | Layered (2048) | 0.5 | 0.147663 |
| ER10 | TOX21_ERa_LUC_VM7_Agonist_10nM_ICI182780 | logistic | Pattern (2048) | 0.5 | 0.264009 |
| ER11 | CCTE_Deisenroth_AIME_96WELL_LUC_Active | logistic | Pattern (2048) | 0.5 | 0.177943 |
| ER12 | CCTE_Deisenroth_AIME_96WELL_LUC_Inactive | xgb | Morgan (1024) | 0.5 | 0.177943 |
| AR01 | NVS_NR_hAR | rf | Morgan (1024) | 0.5 | 0.160316 |
| AR02 | OT_AR_ARSRC1_0960 | dt | MACCS (167) | 0.5 | 0.204822 |
| AR03 | ATG_AR_TRANS | gbt | Layered (2048) | 0.5 | 0.232018 |
| AR04 | TOX21_AR_LUC_MDAKB2_Agonist | rf | Morgan (1024) | 0.5 | 0.262477 |
| AR05 | TOX21_AR_LUC_MDAKB2_Antagonist_0.5nM_R1881 | xgb | Pattern (2048) | 0.5 | 0.264009 |
| AR06 | TOX21_AR_LUC_MDAKB2_Agonist_3uM_Nilutamide | logistic | Morgan (1024) | 0.5 | 0.264009 |
| AR07 | ACEA_AR_antagonist_80hr | dt | Pattern (2048) | 0.5 | 0.205315 |
| T2_UTERO | Uterotrophic agonist response | xgb | Pattern (2048) | 0.5 | 0.115804 |
| T2_HERSH | Hershberger antagonist response | logistic | Pattern (2048) | 0.01 | 0.156458 |
| T3_414 | Prenatal developmental toxicity screening | Random Forest | Morgan (1024) | 0.5 | 0.197151 |
| T3_421 | Reproduction/developmental toxicity screening | Logistic Regression | RDKit (1024) | 0.5 | 0.167623 |
| T3_416 | Two-generation reproductive toxicity | GBT | Layered (2167) | 0.5 | 0.122368 |

Exact settings and artifact SHA256 values: [original manifest](../reference/model_manifest.json).
