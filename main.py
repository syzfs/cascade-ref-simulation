import model
import parametrise
import chx
import cost
import time
import pandas as pd
sep = '%'

# Assumptions (2 refrigerants, 4 temperatures, 4 qualities, 4 component parameters):
Hfluid = 'R1234ze(E)'
Lfluid = 'R23'
T1, T5 = 208, 240                       # in K
T_amb, T_gap, T_overlap = 298, 10, 5    # in K
n_isH, n_isL = 0.75, 0.6
Q_ref = 40000                           # in W
Q1, Q5 = 1, 1       # (ideal saturated vapour streams)
Q3, Q7 = 0, 0       # (ideal saturated liquid streams)
# Thus
assumptions = (Hfluid, Lfluid, T1, T5, T_amb, T_gap, T_overlap, n_isH, n_isL, Q_ref, Q1, Q3, Q5, Q7)

# CHX Modelling-related assumptions
d_hyd = 0.0075          # hydraulic diameter for the CHX, in m

# Costs-related assumptions
area_HTCC = 100*0.186*0.613     # Heat Transfer Area of chosen condenser model
area_LTCE = 40*0.118*0.525      # Heat Transfer Area of chosen evaporator model

# Simulation, Tabulation, Evaluation
print('\n'+sep*80)
print('EN 317 Course Project (Group 3): Cascade Refrigeration Cycle')
print(sep*80)
print('NOTE: Printed results will be rounded for better visibility,')
print('without losing the precision of all the actual computations.')
print(sep*80)
try:
    print('Initialising simulation model with given assumptions...')
    streams, results = model.simulate(*assumptions)
    print('\nSimulation complete. Showing outputs...')
    print('\nTable of Streams, all in SI units (\'Q\' is dryness fraction):')
    print(streams.round(3))
    print('\nTable of Results:')
    print(results)
except:
    print('\nSimulation failed due to bad assumptions, try again!')
print(sep*80)
time.sleep(0.5)
try:
    print('Initialising parametric study over T_amb...')
    parametrise.T_amb(*assumptions)
    print('\nParametric study complete. Plot saved to \'paraTamb.png\'.')
except:
    print('\nParametric study failed due to bad assumptions, try again!')
print(sep*80)
time.sleep(0.5)
try:
    print('Initialising modelling of cascade heat exchanger...')
    results_R1, results_R2, area_CHX = chx.compute_area(streams, T_overlap, Hfluid, Lfluid, d_hyd)
    print('\nModelling complete. Showing results...')
    print('\nRegion 1: LTC fluid is a pure gas, HTC fluid is a mixture')
    print(results_R1)
    print('\nRegion 2: LTC fluid is a mixture, HTC fluid is a mixture')
    print(results_R2)
    print('\nThus, total area required =',str(round(area_CHX,3)),'m^2')
except:
    print('\nModelling failed, try again!')
print(sep*80)
time.sleep(0.5)
try:
    print('Initialising capital cost calculation...')
    c_results, c_TOT = cost.capital(streams, results, area_CHX, area_HTCC, area_LTCE)
    print('\Calculation complete. Showing results...\n')
    print(c_results)
    print('\nThus, total capital cost = ₹',str(round(c_TOT,2)))
    print('After rounding off insignificant digits = ₹',str(round(c_TOT, -5)))
except:
    print('\nCapital cost calculation failed, try again!')
print(sep*80)
print('Execution complete.')
print(sep*80+'\n')