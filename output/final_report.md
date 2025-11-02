# HTA Automation Report – hta_project_04_mdrtb_bpalm

**Generated:** 2025-11-02 11:25:59

## 1. Protocol (parsed)
# HTA Protocol: Cost-Effectiveness of BPaLM / BPaL Regimens versus Conventional Longer MDR/RR-TB Treatment in India

## 1. Background
India has the highest TB burden globally and a substantial burden of drug-resistant TB (DR-TB). WHO has recommended shorter, all-oral regimens such as BPaL (bedaquiline, pretomanid, linezolid) and BPaLM (with moxifloxacin) for MDR/RR-TB under defined eligibility. India is scaling up bedaquiline and all-oral regimens through NTEP. However, the cost of novel drugs is high and program managers require a formal HTA to understand whether the shorter regimens are cost-effective compared with longer conventional MDR-TB regimens.

## 2. Objectives
- **Primary:** To estimate the incremental cost-effectiveness ratio (ICER) of BPaLM (and BPaL) regimens compared with the current standard longer all-oral MDR-TB regimen under NTEP.
- **Secondary:** 
  - To estimate budget impact for NTEP over 5 years under different uptake scenarios.
  - To explore the impact of drug price reductions and domestic procurement.
  - To assess patient-level cost savings (reduced visit/time, adverse events).

## 3. PICO
- **Population:** Patients with MDR/RR-TB meeting WHO/NTEP eligibility criteria for BPaLM/BPaL.
- **Intervention:** BPaLM regimen (Bedaquiline + Pretomanid + Linezolid + Moxifloxacin) – 6 months.
- **Comparator:** Longer MDR-TB regimen (9–18 months) as per current NTEP guidance.
- **Outcomes:** Culture conversion, treatment success, deaths, adverse events, costs (drug, monitoring, AE management), QALYs/DALYs.
- **Perspective:** Programme (NTEP / MoHFW); secondary societal.
- **Time horizon:** 2 years for clinical course + lifetime for disability/death averted.
- **Discounting:** 3% for costs/outcomes.

## 4. Methods

### 4.1 Evidence Review
- Sources: WHO consolidated guidelines on DR-TB, NTEP operational guidelines, DR-TB cohort reports, published trials on BPaL/BPaLM.
- Databases: PubMed, Embase, WHO IRIS, clinicaltrials.gov.
- Keywords: "BPaL", "BPaLM", "bedaquiline", "pretomanid", "linezolid", "drug-resistant tuberculosis", "India", "cost-effectiveness", "all-oral regimen".

### 4.2 Model Structure
- Decision tree for first 24 months:
  - Start treatment → outcomes: success, failure/relapse, death, loss to follow-up, serious AE.
  - Probabilities differ by regimen (shorter vs longer).
- Optional Markov extension for long-term survival with/without sequelae.
- Costs:
  - Drug costs (per regimen, per kg if weight-based).
  - Monitoring: labs, ECG for bedaquiline, AEs (neuropathy, myelosuppression).
  - Hospitalization for severe AE.
- Effectiveness:
  - Treatment success rates from trials and NTEP data.
  - QALY losses for prolonged regimens, AEs, and death.

### 4.3 Economic Evaluation
ICER = (Cost_BPaLM – Cost_long_regimen) / (Effect_BPaLM – Effect_long_regimen)
- Threshold: 50–100% of GDP per capita for India; sensitivity for state-specific thresholds.
- Scenario analyses:
  - Lower price of bedaquiline/pretomanid
  - Higher AE rate for linezolid
  - HIV/TB coinfection subgroup

### 4.4 Budget Impact
- Eligible MDR/RR-TB cases per year from NTEP notifications
- Uptake scenarios: 25%, 50%, 75% on BPaLM
- 5-year horizon
- Output: additional NTEP budget requirement vs status quo

## 5. Outputs
1. Search strategy
2. Evidence/extraction sheet
3. Python decision-tree model
4. BIA spreadsheet
5. Draft manuscript/policy brief for NTEP/HTAIn


## 2. Search Strategy
PubMed search:
(("tuberculosis, multidrug-resistant"[Mesh] OR MDR-TB OR "drug-resistant tuberculosis" OR "RR-TB")
AND (BPaL OR BPaLM OR bedaquiline OR pretomanid OR linezolid OR moxifloxacin)
AND (India OR Indian)
AND (cost OR "economic evaluation" OR "cost-effectiveness" OR HTA OR "budget impact"))
AND ("2005/01/01"[Date - Publication] : "3000"[Date - Publication])

Also screen:
- WHO consolidated guidelines on DR-TB
- NTEP national DR-TB reports
- TB Alliance BPaL publications


## 3. Model Output (stdout)
```
Cost – Long regimen: 141200.0
QALY – Long regimen: 1.321
Cost – BPaLM: 186500.0
QALY – BPaLM: 1.4740000000000002
ICER (INR per QALY): 296078.43137254857

```

## 4. Draft Manuscript (template)
# Draft Manuscript – Cost-Effectiveness of BPaLM Regimen for MDR/RR-TB in India

## Title
Cost-Effectiveness and Budget Impact of Introducing BPaLM Regimens for Drug-Resistant Tuberculosis in India: A Model-Based HTA

## Abstract
Background, Methods, Results, Conclusion – to be auto-filled from model output.

## Sections
1. Introduction – DR-TB burden, NTEP policy shift, WHO BPaL/BPaLM
2. Methods – decision-tree structure, input sources, cost categories, perspective
3. Results – base-case ICER, scenario with lower drug price, BIA for 5 years
4. Discussion – affordability, procurement, implications for NTEP
5. Conclusion – policy recommendation


## 5. Orchestrator Log
```
=== Processing project: hta_project_04_mdrtb_bpalm ===
Protocol: loaded.
Search strings: loaded.
Literature search: starting...
Literature search: completed, extracted 10 data points.
Data processing: starting...
Data processing: completed, filled 10 rows.
R: executed.
R stderr:
â”€â”€ Attaching core tidyverse packages â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse 2.0.0 â”€â”€
âœ” dplyr     1.1.4     âœ” readr     2.1.5
âœ” forcats   1.0.0     âœ” stringr   1.5.2
âœ” ggplot2   4.0.0     âœ” tibble    3.3.0
âœ” lubridate 1.9.4     âœ” tidyr     1.3.1
âœ” purrr     1.1.0     
â”€â”€ Conflicts â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse_conflicts() â”€â”€
âœ– dplyr::filter() masks stats::filter()
âœ– dplyr::lag()    masks stats::lag()
â„¹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors
Error: 'data/mdrtb_bpalm_search_results.csv' does not exist in current working directory ('D:/research-automation/HTA projects').
Execution halted

Model: executed 04_mdrtb_model.py
Model stdout:
Cost – Long regimen: 141200.0
QALY – Long regimen: 1.321
Cost – BPaLM: 186500.0
QALY – BPaLM: 1.4740000000000002
ICER (INR per QALY): 296078.43137254857

Manuscript generation: starting...
Manuscript generation: completed.
```