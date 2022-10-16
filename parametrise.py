import model
import numpy as np
import matplotlib.pyplot as plt

# Parametrize over T_amb
def T_amb(Hfluid, Lfluid, T1, T5, T_amb, T_gap, T_overlap, n_isH, n_isL, Q_ref, Q1, Q3, Q5, Q7):
    T_list = np.linspace(-15,15,31) + T_amb
    COP_list = []
    for T in T_list:
        COP = model.simulate(Hfluid, Lfluid, T1, T5, T, T_gap, T_overlap, n_isH, n_isL, Q_ref, Q1, Q3, Q5, Q7)[1].iloc[7,1]
        COP_list.append(COP)
    plt.plot(T_list-273, COP_list, '.-')
    plt.title('Parametric Study against Ambient Temperature')
    plt.xlabel('Ambient Temperature (in ℃)')
    plt.ylabel('Overall COP')
    plt.savefig('paraTamb')
    return