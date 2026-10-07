# General DART mechanism — 89 models

All 89 use the unified core24 AD procedure. Model weights are preserved from the pinned ChemBAI source. AD references are reconstructed from the frozen core24 ToxCast lineage and local DSSTox exports; missing/rejected structures are recorded in the audit.

| AEID | Assay | Fingerprint | Algorithm | AD references | AD threshold |
|---|---|---|---|---|---|
| 97 | ATG_NRF2_ARE_CIS | Layered | XGBoost | 2877 | 0.23256652 |
| 610 | NVS_GPCR_bAT2 | MACCS | Random Forest | 23 | 0.08668067 |
| 443 | NVS_ENZ_hFGFR1 | MACCS | Logistic | 130 | 0.12781368 |
| 1507 | CCTE_Padilla_ZF_144hpf_TERATOSCORE | Pattern | XGBoost | 551 | 0.18252025 |
| 1682 | STM_H9_CystineISnorm_perc | MACCS | Random Forest | 293 | 0.15864379 |
| 1688 | STM_H9_OrnithineISnorm_perc | Layered | GBT | 293 | 0.15864379 |
| 1690 | STM_H9_OrnCyssISnorm_ratio | RDKit | GBT | 330 | 0.15983812 |
| 3094 | CCTE_Deisenroth_DEVTOX_RUES2-GLR_Endo_Sox17 | Layered | Logistic | 49 | 0.11892842 |
| 3095 | CCTE_Deisenroth_DEVTOX_RUES2-GLR_Endo_Sox2 | MACCS | Random Forest | 49 | 0.11892842 |
| 3096 | CCTE_Deisenroth_DEVTOX_RUES2-GLR_Endo_Bra | RDKit | XGBoost | 49 | 0.11892842 |
| 268 | BSK_KF3CT_MMP9 | Pattern | Logistic | 1306 | 0.20416745 |
| 274 | BSK_KF3CT_TIMP2 | Pattern | GBT | 1306 | 0.20416745 |
| 489 | NVS_ENZ_hMMP13 | Layered | Decision Tree | 64 | 0.09822906 |
| 493 | NVS_ENZ_hMMP3 | MACCS | Random Forest | 80 | 0.11414352 |
| 497 | NVS_ENZ_hMMP9 | Pattern | Random Forest | 171 | 0.14011241 |
| 2869 | BSK_BF4T_MMP9 | Pattern | GBT | 131 | 0.27303492 |
| 579 | NVS_ENZ_hVEGFR3 | Layered | XGBoost | 66 | 0.10997437 |
| 638 | NVS_GPCR_hETA | MACCS | Decision Tree | 31 | 0.09401823 |
| 709 | NVS_NR_bPR | Pattern | Random Forest | 148 | 0.14258404 |
| 2127 | TOX21_PR_BLA_Antagonist_ratio | MACCS | GBT | 5526 | 0.26504793 |
| 2218 | TOX21_PR_BLA_Followup_Agonist_ratio | Pattern | GBT | 173 | 0.17251254 |
| 2219 | TOX21_PR_BLA_Followup_Antagonist_ratio | MACCS | Decision Tree | 173 | 0.17251254 |
| 2222 | TOX21_PR_LUC_Followup_Agonist | MACCS | Logistic | 173 | 0.17251254 |
| 2223 | TOX21_PR_LUC_Followup_Antagonist | RDKit | Logistic | 173 | 0.17251254 |
| 723 | NVS_NR_hRARa_Agonist | MACCS | Logistic | 132 | 0.13669815 |
| 2952 | IUF_NPC5_oligodendrocyte_differentiation_120hr | Layered | XGBoost | 86 | 0.10324374 |
| 2697 | UKN2_HCS_IMR90_neural_migration | Layered | Logistic | 47 | 0.08088801 |
| 1827 | ArunA_Migration_hNP | Layered | Decision Tree | 44 | 0.10262857 |
| 1829 | ArunA_Migration_hNC | Pattern | Decision Tree | 44 | 0.10262857 |
| 1835 | ArunA_NOG_NeuritesPerNeuron | Layered | GBT | 44 | 0.10262857 |
| 2545 | UKN5_HCS_SBAD2_neurite_outgrowth | MACCS | Random Forest | 46 | 0.08410010 |
| 2701 | UKN4_HCS_LUHMES_neurite_outgrowth | Pattern | GBT | 50 | 0.10060362 |
| 2779 | CCTE_Mundy_HCI_Cortical_NOG_NeuriteLength | Pattern | Logistic | 123 | 0.10991763 |
| 2784 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_NeuriteLength | Pattern | XGBoost | 123 | 0.10991763 |
| 2790 | CCTE_Mundy_HCI_hN2_NOG_NeuriteCount | Pattern | Logistic | 56 | 0.09767900 |
| 2791 | CCTE_Mundy_HCI_hN2_NOG_NeuriteLength | Pattern | Logistic | 58 | 0.10308022 |
| 2792 | CCTE_Mundy_HCI_hN2_NOG_NeuronCount | Pattern | Random Forest | 58 | 0.10308022 |
| 3167 | CCTE_Mundy_HCI_iCellGABA_NOG_NeuronCount | Layered | Random Forest | 21 | 0.22638603 |
| 2782 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_CellBodySpotCount | Layered | XGBoost | 123 | 0.10991763 |
| 2786 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_NeuriteSpotCountPerNeuron | Layered | XGBoost | 123 | 0.10991763 |
| 2788 | CCTE_Mundy_HCI_Cortical_Synap&Neur_Matur_SynapseCount | MACCS | Logistic | 123 | 0.10991763 |
| 2793 | CCTE_Mundy_HCI_hNP1_Casp3_7 | Pattern | Logistic | 172 | 0.13404227 |
| 2529 | CCTE_Shafer_MEA_dev_LDH | MACCS | XGBoost | 291 | 0.14994485 |
| 2530 | CCTE_Shafer_MEA_dev_AB | MACCS | Logistic | 291 | 0.14994485 |
| 2547 | UKN5_HCS_SBAD2_cell_viability | MACCS | Random Forest | 46 | 0.08410010 |
| 2699 | UKN2_HCS_IMR90_cell_viability | Layered | Random Forest | 47 | 0.08088801 |
| 674 | NVS_GPCR_rmMGluR1 | MACCS | XGBoost | 20 | 0.09120730 |
| 601 | NVS_ENZ_rMAOAC | Morgan | Logistic | 147 | 0.15111409 |
| 603 | NVS_ENZ_rMAOAP | Pattern | Random Forest | 79 | 0.12692411 |
| 605 | NVS_ENZ_rMAOBC | RDKit | Logistic | 102 | 0.13316201 |
| 607 | NVS_ENZ_rMAOBP | MACCS | Logistic | 102 | 0.12742095 |
| 597 | NVS_ENZ_rCOMT | MACCS | Logistic | 47 | 0.11192033 |
| 734 | NVS_TR_hSERT | Layered | Decision Tree | 79 | 0.11948697 |
| 737 | NVS_TR_rSERT | Layered | Logistic | 113 | 0.14592378 |
| 2498 | CCTE_Shafer_MEA_dev_active_electrodes_number | Layered | Random Forest | 291 | 0.14994485 |
| 2500 | CCTE_Shafer_MEA_dev_bursting_electrodes_number | Layered | Random Forest | 291 | 0.14994485 |
| 2504 | CCTE_Shafer_MEA_dev_per_burst_spike_percent | RDKit | GBT | 291 | 0.14994485 |
| 2508 | CCTE_Shafer_MEA_dev_interburst_interval_mean | RDKit | Logistic | 291 | 0.14994485 |
| 2512 | CCTE_Shafer_MEA_dev_network_spike_peak | MACCS | XGBoost | 291 | 0.14994485 |
| 2514 | CCTE_Shafer_MEA_dev_spike_duration_mean | Layered | Logistic | 291 | 0.14994485 |
| 2516 | CCTE_Shafer_MEA_dev_network_spike_duration_std | Layered | XGBoost | 291 | 0.14994485 |
| 2520 | CCTE_Shafer_MEA_dev_per_network_spike_spike_number_mean | MACCS | XGBoost | 291 | 0.14994485 |
| 2522 | CCTE_Shafer_MEA_dev_per_network_spike_spike_percent | MACCS | Random Forest | 291 | 0.14994485 |
| 2524 | CCTE_Shafer_MEA_dev_correlation_coefficient_mean | Pattern | XGBoost | 291 | 0.14994485 |
| 2526 | CCTE_Shafer_MEA_dev_mutual_information_norm | Pattern | Logistic | 291 | 0.14994485 |
| 614 | NVS_GPCR_g5HT4 | Pattern | Random Forest | 104 | 0.14801037 |
| 622 | NVS_GPCR_h5HT2A | MACCS | XGBoost | 82 | 0.12092289 |
| 623 | NVS_GPCR_h5HT5A | MACCS | Logistic | 120 | 0.16055328 |
| 624 | NVS_GPCR_h5HT6 | Layered | Logistic | 76 | 0.12514840 |
| 625 | NVS_GPCR_h5HT7 | Layered | Decision Tree | 120 | 0.14188068 |
| 659 | NVS_GPCR_p5HT2C | Layered | Random Forest | 87 | 0.14994603 |
| 660 | NVS_GPCR_r5HT_NonSelective | Layered | GBT | 69 | 0.12717368 |
| 661 | NVS_GPCR_r5HT1_NonSelective | Pattern | Logistic | 53 | 0.11202130 |
| 319 | NVS_ADME_hCYP19A1 | MACCS | GBT | 186 | 0.14745630 |
| 321 | NVS_ADME_hCYP1A1 | Pattern | Decision Tree | 135 | 0.14811887 |
| 706 | NVS_MP_hPBR | RDKit | GBT | 337 | 0.18015221 |
| 707 | NVS_MP_rPBR | Pattern | GBT | 333 | 0.17173897 |
| 891 | CEETOX_H295R_11DCORT | MACCS | XGBoost | 449 | 0.17067315 |
| 895 | CEETOX_H295R_OHPROG | Layered | Decision Tree | 449 | 0.17067315 |
| 913 | CEETOX_H295R_PROG | Morgan | Logistic | 449 | 0.17067315 |
| 2143 | CEETOX_H295R_11DCORT_noMTC | Layered | Decision Tree | 64 | 0.09398226 |
| 2145 | CEETOX_H295R_OHPREG_noMTC | Morgan | Decision Tree | 64 | 0.09398226 |
| 2147 | CEETOX_H295R_OHPROG_noMTC | Pattern | XGBoost | 64 | 0.09398226 |
| 2149 | CEETOX_H295R_ANDR_noMTC | Pattern | Random Forest | 64 | 0.09398226 |
| 2153 | CEETOX_H295R_CORTISOL_noMTC | MACCS | XGBoost | 64 | 0.09398226 |
| 2157 | CEETOX_H295R_DOC_noMTC | Morgan | Decision Tree | 64 | 0.09398226 |
| 2165 | CEETOX_H295R_PROG_noMTC | MACCS | Decision Tree | 64 | 0.09398226 |
| 3078 | CCTE_Deisenroth_5AR_NBTE_ratio | MACCS | XGBoost | 164 | 0.14865039 |
| 3161 | CCTE_Deisenroth_H295R-HTRF_384WELL_ESTRADIOL | Layered | GBT | 28 | 0.13559464 |
