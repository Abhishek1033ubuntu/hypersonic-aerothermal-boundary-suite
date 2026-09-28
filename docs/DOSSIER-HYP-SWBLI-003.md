# ENGINEERING DOSSIER: HYP-SWBLI-003
**Subject:** Grand Challenge 2 - Hypersonic Aerothermal Transition & SWBLI Mitigation
**Regime:** Mach 5.6 (1,900 m/s)
**Trajectory:** 50 km (Low-to-Mid Altitude)

## 1. Baseline Problem Matrix
An oblique shock wave ($P_2/P_1 \approx 8.5$) impinging on a hypersonic projectile body at 1,900 m/s induces catastrophic fluid-structure failures:
* **Aerodynamic Drag:** Base skin-friction is highly elevated. Viscoelastic "Jello-like" sacrificial coatings fail completely due to Kelvin-Helmholtz melt-wave stripping, causing a +315% drag spike.
* **Flow Separation:** The adverse pressure gradient forces boundary-layer detachment, creating a 120 mm unsteady recirculation bubble.
* **Thermal Shock:** Shear-layer reattachment generates a localized convective heat flux peak of 11.08 MW/m².
* **Vibro-Acoustic Hammering:** The reattachment unsteadiness transmits 498.8 MPa high-frequency stress waves into the airframe.

## 2. The 3-Pillar Hybrid Architecture

### Pillar 1: Light-Gas Sublimating Coating
* **Material:** $MgH_2$-doped elastomeric matrix ($H_{eff} = 5.70$ MJ/kg, $M_{gas} = 2.0$ g/mol).
* **Geometry:** Axially graded thickness (5.0 mm at nose $\rightarrow$ 1.5 mm at tail).
* **Mechanism:** Direct solid-to-gas phase sublimation injects pure $H_2$ into the inner boundary layer, expanding the shear layer outward.
* **Result:** Achieves a uniform 33.1% reduction in overall skin-friction drag with a minimal total mass penalty of 2.73 kg over a 50 km flight.

### Pillar 2: NS-DBD Plasma Actuation
* **Actuation Array:** Positioned at $x = 0.61$ m (just upstream of the shock root).
* **Mechanism:** High-voltage nanosecond pulses generate localized thermal micro-jets, re-energizing the subsonic boundary layer with freestream momentum.
* **Result:** Collapses the separation bubble from 120 mm to <15 mm. Reduces peak reattachment heat flux by 60.7% (11.08 MW/m² $\rightarrow$ 4.35 MW/m²).

### Pillar 3: Bio-Mimetic Fe-SMA Internal Skeleton
* **Material:** `Fe-28Mn-6Si-5Cr-0.5C` lattice.
* **Mechanism:** Dissipates kinetic shock energy through stress-induced $\gamma \rightleftharpoons \varepsilon$ phase transformations.
* **Result:** Absorbs 1.720 MJ/m³ of mechanical strain energy, damping internal stress wave amplitudes from 498.8 MPa down to 212.8 MPa, preventing structural resonance and fatigue.
