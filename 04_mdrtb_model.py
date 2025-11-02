"""Decision-tree HTA model: BPaLM vs longer MDR-TB regimen (India)
Replace placeholder probabilities and costs with values from 03_data_extraction_template.csv
"""

import math

discount_rate = 0.03

# --- Placeholder inputs ---
# Conventional regimen (longer)
p_success_long = 0.65
p_death_long = 0.12
p_ltfu_long = 0.10
p_failure_long = 0.13

cost_drug_long = 120000   # INR total regimen
cost_monitor_long = 20000
cost_ae_long = 8000

# BPaLM regimen
p_success_bpalm = 0.80
p_death_bpalm = 0.08
p_ltfu_bpalm = 0.05
p_failure_bpalm = 0.07

cost_drug_bpalm = 160000   # higher drug cost
cost_monitor_bpalm = 25000
cost_ae_bpalm = 10000

# utility weights (placeholder)
u_success = 0.85
u_failure = 0.6
u_death = 0.0

def expected_cost_effect(p_s, p_d, p_l, p_f, c_drug, c_mon, c_ae):
    # assume AE in fraction of patients
    ae_prob = 0.15
    cost = c_drug + c_mon + ae_prob * c_ae
    # outcomes converted to QALYs over 2 years
    qaly = (
        p_s * u_success * 2
        + p_f * u_failure * 2
        + p_l * u_failure * 1
        + p_d * u_death * 0
    )
    return cost, qaly

if __name__ == "__main__":
    cost_long, qaly_long = expected_cost_effect(
        p_success_long, p_death_long, p_ltfu_long, p_failure_long,
        cost_drug_long, cost_monitor_long, cost_ae_long
    )
    cost_bpalm, qaly_bpalm = expected_cost_effect(
        p_success_bpalm, p_death_bpalm, p_ltfu_bpalm, p_failure_bpalm,
        cost_drug_bpalm, cost_monitor_bpalm, cost_ae_bpalm
    )
    incr_cost = cost_bpalm - cost_long
    incr_qaly = qaly_bpalm - qaly_long
    icer = incr_cost / incr_qaly if incr_qaly != 0 else None
    print("Cost – Long regimen:", cost_long)
    print("QALY – Long regimen:", qaly_long)
    print("Cost – BPaLM:", cost_bpalm)
    print("QALY – BPaLM:", qaly_bpalm)
    print("ICER (INR per QALY):", icer)
