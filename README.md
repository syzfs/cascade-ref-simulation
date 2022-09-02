# Cascade Vapour Compression Refrigeration Cycle
## (a thermodynamic simulation using CoolProp on Python)
This repository contains the files used by Group 3 in part 2 of the Course Project for EN 317 (Thermo-Fluid Devices).
```
cascade-ref-simulation
├── README.md
|
├── main.py           <- The only executable file.
|                        Sets all the assumed input parameters.
|                        Generates the output.
|                        Broad simple overview of the program execution.
|
├── model.py          <- All thermodynamic equations, and compilation of results.
|                        Invoked by main.py and parametrise.py.
|
├── parametrise.py    <- Varies the ambient temperature and plots the change in COP.
|                        Invoked by executing main.py.
|
└── shorthands.py     <- Syntactical shortening of CoolProp functions.
                         Invoked inside model.py.
```

**Python libraries needed:** `CoolProp`, `matplotlib`, `numpy`, `pandas`
