import model
import parametrise

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

# Simulation, Tabulation, Evaluation
try:
    print('\nFeeding assumptions to model...')
    streams, results = model.simulate(*assumptions)
    print('\nSimulation complete. Showing outputs...')
    print('\nTable of Streams, all in SI units (\'Q\' is dryness fraction):')
    print(streams)
    print('\nTable of Results:')
    print(results)
    print('\nInitialising parametric study over T_amb...')
    parametrise.T_amb(*assumptions)
    print('\nParametric study complete. Plot saved to \'paraTamb.png\'.')
except:
    print('Simulation failed due to bad assumptions, try again!')