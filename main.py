import model
import parametrise
import chx
import time

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
d_pipe = 0.04       # internal pipe diameter, in m
chev_theta = 45
# any assumed variables required?

# Costs-related assumptions
n_elH, n_elL = 0.8, 0.8         # Change this after literature review!
rate_el = -0.01

# Simulation, Tabulation, Evaluation
try:
    print('\nInitialising simulation model with given assumptions...')
    streams, results = model.simulate(*assumptions)
    print('\nSimulation complete. Showing outputs...')
    print('\nTable of Streams, all in SI units (\'Q\' is dryness fraction):')
    print(streams)
    print('\nTable of Results:')
    print(results)
except:
    print('\nSimulation failed due to bad assumptions, try again!')
time.sleep(0.5)
try:
    print('\nInitialising parametric study over T_amb...')
    parametrise.T_amb(*assumptions)
    print('\nParametric study complete. Plot saved to \'paraTamb.png\'.')
except:
    print('\nParametric study failed due to bad assumptions, try again!')
time.sleep(0.5)
try:
    print('\nInitialising modelling of cascade heat exchanger...')
    chx.compute_area(streams, Hfluid, Lfluid, d_pipe, chev_theta)
except:
    print('\nModelling failed, try again!')