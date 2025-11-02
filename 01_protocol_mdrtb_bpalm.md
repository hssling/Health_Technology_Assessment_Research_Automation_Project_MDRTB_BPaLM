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
