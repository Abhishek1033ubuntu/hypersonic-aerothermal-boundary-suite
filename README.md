# Hypersonic Aerothermal Boundary-Layer Transition & SWBLI Mitigation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.PENDING.svg)](https://doi.org/10.5281/zenodo.PENDING) 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Abhishek1033ubuntu/hypersonic-aerothermal-boundary-suite/blob/main/notebooks/hypersonic_swbli_sim.ipynb) 
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg) 
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) 

A comprehensive multi-physics simulation suite designed to resolve Shockwave Boundary-Layer Interaction (SWBLI) and aerothermal transition on hypersonic projectiles (Mach > 5).

## Overview
At speeds exceeding Mach 5 (1,900 m/s), severe aerothermal heating and oblique shock wave impingement cause boundary layer detachment, extreme drag spikes, and structural vibro-acoustic hammering. This repository provides a unified 3-pillar engineering solution:

1. **Passive Aerodynamic Drag Mitigation:** Axially graded Magnesium-Hydride ($MgH_2$) sublimating coating for boundary-layer gas blowing.
2. **Active SWBLI Control:** Nanosecond Pulsed Dielectric Barrier Discharge (NS-DBD) plasma actuation array to collapse separation bubbles.
3. **Internal Structural Damping:** Bio-mimetic `Fe-28Mn-6Si-5Cr-0.5C` Shape Memory Alloy (SMA) internal lattice for mechanical stress wave dissipation.

## Quick Start
Run the master simulation to visualize the integrated physical response:
```bash
python src/hypersonic_master_sim.py
```

# Citation
If you utilize this computational framework, please cite:
Singh, A. (2026). Hypersonic Aerothermal Boundary-Layer Transition & SWBLI Mitigation Suite (Version 1.0.0).
