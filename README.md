# cascade-ref-simulation
This repository contains the files used by Group 10 in part 2 of the Course Project for EN 317 (Thermo-Fluid Devices).

1. `main.py`  
- The only file you will have to run.
- You can change any of the assumed values, refrigerants, etc. to simulate the same model under different assumptions.

2. `model.py`
- The file which contains the actual thermodynamic equations used for computation of all values.
- Returns a stream-wise dataframe containing all the calculated & assumed variables, and another dataframe containing the values of all the overaall performance parameters of the system.

3. `shorthands.py`
- Replaces inconvenient CoolProp function names (and syntax) with our own, shorter, more intuitive (and consistent) versions.

**Python libraries needed:** `CoolProp`, `matplotlib`, `pandas`
