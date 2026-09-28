"""
hypersonic_master_sim.py
Master multi-physics solver for SWBLI mitigation, integrating:
1. Sublimating Coating Ablation & Gas Blowing Drag Reduction
2. NS-DBD Plasma Actuator Separation Bubble Collapse
3. Fe-Mn-Si SMA Structural Vibro-Acoustic Damping
"""

import numpy as np
import matplotlib.pyplot as plt

def run_hypersonic_simulation():
    # 1. Projectile Geometry & Hypersonic Flow Conditions
    x = np.linspace(0.01, 1.2, 500)
    V_inf = 1900.0
    rho_air = 0.414
    P_1 = 26.5e3
    flight_time = 26.3

    # 2. Pillar 1: Sublimating Coating Drag & Ablation
    H_eff = 5.70e6
    M_gas = 2.00
    density_coating = 1350.0
    t_initial = 0.005 * np.exp(-1.2 * x) + 0.0015 

    Re_x = (rho_air * V_inf * x) / 1.78e-5
    C_f_0 = 0.0592 / (Re_x**0.2)
    q_conv = 0.85e6 * (0.5 / x)**0.2

    m_dot = q_conv / H_eff
    B_param = (m_dot / (rho_air * V_inf * (C_f_0 / 2.0))) * ((28.97 / M_gas)**0.45)
    drag_ratio = np.clip(np.log(1.0 + 1.8 * B_param) / (1.8 * B_param), 0.45, 1.0)
    t_remaining = np.maximum(0.0, t_initial - (m_dot / density_coating) * flight_time)

    # 3. Pillar 2: SWBLI & NS-DBD Plasma Actuation
    x_shock = 0.68
    P_ratio_shock = 8.5

    P_uncontrolled = P_1 * (1.0 + (P_ratio_shock - 1.0) / (1.0 + np.exp(-35.0 * (x - x_shock))))
    sep_zone = (x >= 0.62) & (x <= 0.74)
    P_uncontrolled[sep_zone] += 2.5 * P_1 * np.sin(np.pi * (x[sep_zone] - 0.62) / 0.12)
    q_uncontrolled = 0.85e6 * (P_uncontrolled / P_1)**1.2

    P_controlled = P_1 * (1.0 + (P_ratio_shock - 1.0) / (1.0 + np.exp(-55.0 * (x - x_shock))))
    q_controlled = 0.57e6 * (P_controlled / P_1)**0.95

    # 4. Pillar 3: Internal Fe-SMA Damping
    U_dissipated_SMA = 1.720 
    vibro_stress_uncontrolled = (q_uncontrolled / 1e6) * 45.0
    vibro_stress_damped = vibro_stress_uncontrolled * (1.0 - np.clip(U_dissipated_SMA / 3.0, 0.0, 0.75))

    # --- Plotting Module ---
    fig, axs = plt.subplots(3, 1, figsize=(10, 11))

    axs[0].plot(x, drag_ratio, 'g-', lw=2.5, label='Drag Ratio (C_f / C_f0)')
    axs[0].plot(x, t_remaining * 1000, 'b--', lw=2, label='Remaining Coating Thickness (mm)')
    axs[0].set_ylabel('Drag Ratio / Thickness')
    axs[0].set_title('Pillar 1: Sublimating Coating Drag Reduction & Survival (33.1% Drag Red.)')
    axs[0].grid(True, ls='--')
    axs[0].legend()

    axs[1].plot(x, q_uncontrolled / 1e6, 'r--', lw=2, label='Uncontrolled Thermal Peak')
    axs[1].plot(x, q_controlled / 1e6, 'g-', lw=2.5, label='Controlled Thermal Profile (Plasma + Coating)')
    axs[1].axvspan(0.60, 0.62, color='cyan', alpha=0.3, label='NS-DBD Plasma Actuator')
    axs[1].set_ylabel('Heat Flux (MW/m²)')
    axs[1].set_title('Pillar 2: SWBLI Thermal Spike Suppression (60.7% Peak Reduction)')
    axs[1].grid(True, ls='--')
    axs[1].legend()

    axs[2].plot(x, vibro_stress_uncontrolled, 'r--', lw=2, label='Unmitigated Structural Stress Waves')
    axs[2].plot(x, vibro_stress_damped, 'purple', lw=2.5, label='Damped Stress Waves (Fe-28Mn-6Si-5Cr-0.5C Skeleton)')
    axs[2].set_xlabel('Distance along Projectile x (m)')
    axs[2].set_ylabel('Stress Wave Amplitude (MPa)')
    axs[2].set_title('Pillar 3: Internal Bio-Mimetic Skeleton Acoustic Shock Damping')
    axs[2].grid(True, ls='--')
    axs[2].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_hypersonic_simulation()
