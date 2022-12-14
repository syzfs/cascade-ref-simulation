# Cascade Vapour Compression Refrigeration Cycle
## (thermodynamic simulation using `CoolProp`, and modelling using `ht`, on Python)
This repository contains the files used by Group 3, in Parts 2 & 3 of the Course Project for EN 317 (Thermo-Fluid Devices).
```
cascade-ref-simulation
├── README.md         <- This file (added for the reader's convenience).
|
├── chx.py            <- Physically models the cascade heat exchanger based on the simulation results.
                         Invoked by executing main.py.
|
├── cost.py           <- Computes the total capital cost using suitable cost functions.
                         Invoked by executing main.py.
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
├── shorthands.py     <- Syntactical shortening of CoolProp functions.
|                        Invoked inside model.py.
|
├── paraTamb.png      <- Graphical output of the parametric study.
|                        Generated by invoking parametrise.py.
|
├── CP2 G03.pdf       <- The report for Part 2 of the project (modelling and simulation).
|
└── CP3 G03.pdf       <- The report for Part 3 of the project (techno-economic analysis).
```

**Python libraries needed:** `CoolProp`, `matplotlib`, `numpy`, `pandas`
