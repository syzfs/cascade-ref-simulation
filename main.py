import model

# Assumptions (2 refrigerants, 4 temperatures, 4 qualities, 4 component parameters):
Hfluid = 'R1234ze(E)'
Lfluid = 'R23'
T1, T5, T7 = 208, 237, 303          # in K
T_overlap = 5                       # in K
n_isH, n_isL = 0.75, 0.6
Q_ref = 40000                       # in W
Q1, Q5 = 1, 1       # (ideal saturated vapour streams)
Q3, Q7 = 0, 0       # (ideal saturated liquid streams)
# Thus
assumptions = (Hfluid, Lfluid, T1, T5, T7, T_overlap, n_isH, n_isL, Q_ref, Q1, Q3, Q5, Q7)

# Simulation, Tabulation, Evaluation
try:
    streams, results = model.simulate(*assumptions)
    print('Table of Results, all in SI units (\'Q\' is dryness fraction):')
    print(streams)
    print(results)
except:
    print('Simulation failed due to bad assumptions, try again!')