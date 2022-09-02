# Cascade Vapour Compression Refrigeration Cycle
## (a thermodynamic simulation using CoolProp on Python)
This repository contains the files used by Group 3 in part 2 of the Course Project for EN 317 (Thermo-Fluid Devices).
```
cascade-ref-simulation
├── README.md
|
├── main.py           <- The only executable file, with all assumed values/parameters.
|                        Generates the output.
|                        Broad simple overview of the program execution.
|
├── model.py          <- All thermodynamic equations, and compilation of results.
|                        Invoked by executing main.py.
|
└── shorthands.py     <- Syntactical shortening of CoolProp functions.
```

1. `main.py`  
- The only file you will have to run.
- You can change any of the assumed values, refrigerants, etc. to simulate the same model under different assumptions.

2. `model.py`
- The file which contains the actual thermodynamic equations used for computation of all values.
- Returns a stream-wise dataframe containing all the calculated & assumed variables, and another dataframe containing the values of all the overall performance parameters of the system.

3. `shorthands.py`
- Replaces inconvenient CoolProp function names (and syntax) with our own, shorter, more intuitive (and consistent) versions.

**Python libraries needed:** `CoolProp`, `matplotlib`, `pandas`
