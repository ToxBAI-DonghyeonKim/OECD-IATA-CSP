# General DART mechanism — 89 models

Selected from the agreed Table2 89-assay list, matched to ChemBAI ToxCast_model(F1). Each file was checked against the pinned Git blob SHA and loaded for inference.

Source commit: `656171a39b6caf5e57afcaf0acdbd082c3622e70`. AD references/cutoffs are not supplied by these source artifacts; DART outputs are raw predictions.

| AEID | Assay | Fingerprint | Algorithm | F1 |
|---|---|---|---|---|
| 97 | ATG_NRF2_ARE_CIS | Layered | XGBoost | 0.56 |
| 610 | NVS_GPCR_bAT2 | MACCS | Random Forest | 0.73 |
| 443 | NVS_ENZ_hFGFR1 | MACCS | Logistic | 0.55 |
| 1507 | CCTE_Padilla_ZF_144hpf_TERATOSCORE | Pattern | XGBoost | 0.82 |
| 1682 | STM_H9_CystineISnorm_perc | MACCS | Random Forest | 0.52 |
| 1688 | STM_H9_OrnithineISnorm_perc | Layered | GBT | 0.5 |
| 1690 | STM_H9_OrnCyssISnorm_ratio | RDKit | GBT | 0.58 |
| 3094 | CCTE_Deisenroth_DEVTOX_RUES2-GLR_Endo_Sox17 | Layered | Logistic | 0.79 |
| 3095 | CCTE_Deisenroth_DEVTOX_RUES2-GLR_Endo_Sox2 | MACCS | Random Forest | 0.75 |
| 3096 | CCTE_Deisenroth_DEVTOX_RUES2-GLR_Endo_Bra | RDKit | XGBoost | 0.7 |
| 268 | BSK_KF3CT_MMP9 | Pattern | Logistic | 0.52 |
| 274 | BSK_KF3CT_TIMP2 | Pattern | GBT | 0.5 |
| 489 | NVS_ENZ_hMMP13 | Layered | Decision Tree | 0.74 |
| 493 | NVS_ENZ_hMMP3 | MACCS | Random Forest | 0.62 |
| 497 | NVS_ENZ_hMMP9 | Pattern | Random Forest | 0.61 |
| 2869 | BSK_BF4T_MMP9 | Pattern | GBT | 0.51 |
| 579 | NVS_ENZ_hVEGFR3 | Layered | XGBoost | 0.51 |
| 638 | NVS_GPCR_hETA | MACCS | Decision Tree | 0.63 |
| 709 | NVS_NR_bPR | Pattern | Random Forest | 0.64 |
| 2127 | TOX21_PR_BLA_Antagonist_ratio | MACCS | GBT | 0.6 |
| 2218 | TOX21_PR_BLA_Followup_Agonist_ratio | Pattern | GBT | 0.83 |
| 2219 | TOX21_PR_BLA_Followup_Antagonist_ratio | MACCS | Decision Tree | 0.78 |
| 2222 | TOX21_PR_LUC_Followup_Agonist | MACCS | Logistic | 0.9 |
| 2223 | TOX21_PR_LUC_Followup_Antagonist | RDKit | Logistic | 0.73 |
| 723 | NVS_NR_hRARa_Agonist | MACCS | Logistic | 0.56 |
| 2952 | IUF_NPC5_oligodendrocyte_differentiation_120hr | Layered | XGBoost | 0.51 |
| 2697 | UKN2_HCS_IMR90_neural_migration | Layered | Logistic | 0.58 |
| 1827 | ArunA_Migration_hNP | Layered | Decision Tree | 0.64 |
| 1829 | ArunA_Migration_hNC | Pattern | Decision Tree | 0.6 |
| 1835 | ArunA_NOG_NeuritesPerNeuron | Layered | GBT | 0.5 |
| 2545 | UKN5_HCS_SBAD2_neurite_outgrowth | MACCS | Random Forest | 0.66 |
| 2701 | UKN4_HCS_LUHMES_neurite_outgrowth | Pattern | GBT | 0.55 |
| 2779 | CCTE_Mundy_HCI_Cortical_NOG_NeuriteLength | Pattern | Logistic | 0.5 |
| 2784 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_NeuriteLength | Pattern | XGBoost | 0.53 |
| 2790 | CCTE_Mundy_HCI_hN2_NOG_NeuriteCount | Pattern | Logistic | 0.59 |
| 2791 | CCTE_Mundy_HCI_hN2_NOG_NeuriteLength | Pattern | Logistic | 0.58 |
| 2792 | CCTE_Mundy_HCI_hN2_NOG_NeuronCount | Pattern | Random Forest | 0.58 |
| 3167 | CCTE_Mundy_HCI_iCellGABA_NOG_NeuronCount | Layered | Random Forest | 0.56 |
| 2782 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_CellBodySpotCount | Layered | XGBoost | 0.59 |
| 2786 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_NeuriteSpotCountPerNeuron | Layered | XGBoost | 0.57 |
| 2788 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_SynapseCount | MACCS | Logistic | 0.59 |
| 2793 | CCTE_Mundy_HCI_hNP1_Casp3_7 | Pattern | Logistic | 0.52 |
| 2529 | CCTE_Shafer_MEA_dev_LDH | MACCS | XGBoost | 0.62 |
| 2530 | CCTE_Shafer_MEA_dev_AB | MACCS | Logistic | 0.52 |
| 2547 | UKN5_HCS_SBAD2_cell_viability | MACCS | Random Forest | 0.66 |
| 2699 | UKN2_HCS_IMR90_cell_viability | Layered | Random Forest | 0.51 |
| 674 | NVS_GPCR_rmMGluR1 | MACCS | XGBoost | 0.63 |
| 601 | NVS_ENZ_rMAOAC | Morgan | Logistic | 0.81 |
| 603 | NVS_ENZ_rMAOAP | Pattern | Random Forest | 0.71 |
| 605 | NVS_ENZ_rMAOBC | RDKit | Logistic | 0.63 |
| 607 | NVS_ENZ_rMAOBP | MACCS | Logistic | 0.57 |
| 597 | NVS_ENZ_rCOMT | MACCS | Logistic | 0.62 |
| 734 | NVS_TR_hSERT | Layered | Decision Tree | 0.6 |
| 737 | NVS_TR_rSERT | Layered | Logistic | 0.66 |
| 2498 | CCTE_Shafer_MEA_dev_active_electrodes_number | Layered | Random Forest | 0.66 |
| 2500 | CCTE_Shafer_MEA_dev_bursting_electrodes_number | Layered | Random Forest | 0.67 |
| 2504 | CCTE_Shafer_MEA_dev_per_burst_spike_percent | RDKit | GBT | 0.62 |
| 2508 | CCTE_Shafer_MEA_dev_interburst_interval_mean | RDKit | Logistic | 0.57 |
| 2512 | CCTE_Shafer_MEA_dev_network_spike_peak | MACCS | XGBoost | 0.68 |
| 2514 | CCTE_Shafer_MEA_dev_spike_duration_mean | Layered | Logistic | 0.68 |
| 2516 | CCTE_Shafer_MEA_dev_network_spike_duration_std | Layered | XGBoost | 0.51 |
| 2520 | CCTE_Shafer_MEA_dev_per_network_spike_spike_number_mean | MACCS | XGBoost | 0.58 |
| 2522 | CCTE_Shafer_MEA_dev_per_network_spike_spike_percent | MACCS | Random Forest | 0.66 |
| 2524 | CCTE_Shafer_MEA_dev_correlation_coefficient_mean | Pattern | XGBoost | 0.65 |
| 2526 | CCTE_Shafer_MEA_dev_mutual_information_norm | Pattern | Logistic | 0.58 |
| 614 | NVS_GPCR_g5HT4 | Pattern | Random Forest | 0.72 |
| 622 | NVS_GPCR_h5HT2A | MACCS | XGBoost | 0.79 |
| 623 | NVS_GPCR_h5HT5A | MACCS | Logistic | 0.66 |
| 624 | NVS_GPCR_h5HT6 | Layered | Logistic | 0.73 |
| 625 | NVS_GPCR_h5HT7 | Layered | Decision Tree | 0.72 |
| 659 | NVS_GPCR_p5HT2C | Layered | Random Forest | 0.8 |
| 660 | NVS_GPCR_r5HT_NonSelective | Layered | GBT | 0.67 |
| 661 | NVS_GPCR_r5HT1_NonSelective | Pattern | Logistic | 0.58 |
| 319 | NVS_ADME_hCYP19A1 | MACCS | GBT | 0.51 |
| 321 | NVS_ADME_hCYP1A1 | Pattern | Decision Tree | 0.68 |
| 706 | NVS_MP_hPBR | RDKit | GBT | 0.69 |
| 707 | NVS_MP_rPBR | Pattern | GBT | 0.73 |
| 891 | CEETOX_H295R_11DCORT | MACCS | XGBoost | 0.59 |
| 895 | CEETOX_H295R_OHPROG | Layered | Decision Tree | 0.66 |
| 913 | CEETOX_H295R_PROG | Morgan | Logistic | 0.53 |
| 2143 | CEETOX_H295R_11DCORT_noMTC | Layered | Decision Tree | 0.6 |
| 2145 | CEETOX_H295R_OHPREG_noMTC | Morgan | Decision Tree | 0.53 |
| 2147 | CEETOX_H295R_OHPROG_noMTC | Pattern | XGBoost | 0.59 |
| 2149 | CEETOX_H295R_ANDR_noMTC | Pattern | Random Forest | 0.54 |
| 2153 | CEETOX_H295R_CORTISOL_noMTC | MACCS | XGBoost | 0.5 |
| 2157 | CEETOX_H295R_DOC_noMTC | Morgan | Decision Tree | 0.56 |
| 2165 | CEETOX_H295R_PROG_noMTC | MACCS | Decision Tree | 0.53 |
| 3078 | CCTE_Deisenroth_5AR_NBTE_ratio | MACCS | XGBoost | 0.74 |
| 3161 | CCTE_Deisenroth_H295R-HTRF_384WELL_ESTRADIOL | Layered | GBT | 0.53 |
