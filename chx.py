from shorthands import *
from ht import *
# import numpy as np
import math
import pandas as pd

def compute_area(streams, Hfluid, Lfluid, d_pipe, chev_theta):
    area_NET = 0                    # Initialise the summation term

    # Region 1: LTC gas, HTC mixture
    print('\nRegion 1: LTC fluid is a pure gas, HTC fluid is a mixture')
    mdot_L = streams['mdot'][2]
    P_L = streams['P'][2]                           # Pressure in LTC stays at P2, throughout the CHX
    h2 = streams['h'][2]                            # Specific enthalpy of LTC fluid at the Region 1 inlet
    h2_cool = HST_from_PQ(P_L, 1, Lfluid)[0]        # Specific enthalpy of LTC fluid at the Region 1 endpoint
    Qdot_R1 = mdot_L*(h2-h2_cool)
    # print('Rate of heat transfer in Region 1 =',str(Qdot_R1),'W')

    T2 = streams['T'][2]
    T3 = streams['T'][3]
    T_L = (T2+T3)/2             # Take average of T2 and T3
    D_L, V_L, L_L, C_L = cp.PropsSI(['D', 'V', 'L', 'C'], 'P', P_L, 'T', T_L, Lfluid)

    v_L = mdot_L/(0.25*math.pi*d_pipe*d_pipe)
    Re_L = (D_L*v_L*d_pipe)/V_L
    Pr_L = (C_L*V_L)/L_L
    Nu_L = Nu_plate_Kumar(Re=Re_L, Pr=Pr_L, chevron_angle=chev_theta)
    h_L_R1 = Nu_L*L_L/d_pipe
    # Found convective heat transfer coefficient on LTC side!
    # print('Convective heat transfer coefficient on LTC side =',str(h_L_R1),'W/(m^2 K)')

    P_H = streams['P'][8]      # Pressure stays at P8, throughout Region 1
    T_H = streams['T'][8]      # Temperature stays at T8
    mdot_H = streams['mdot'][8]
    h8 = streams['h'][8]                            # Specific enthalpy of HTC fluid at the Region 1 inlet
    h8_heat = h8 + (Qdot_R1/mdot_H) # Specific enthalpy of HTC fluid at the Region 1 endpoint
    Q8 = streams['Q'][8]                            # Quality of HTC fluid at Region 1 inlet
    Q8_heat = Q_from_PH(P_H, h8_heat, Hfluid)       # Quality of HTC fluid at Region 1 endpoint
    Q_H_R1 = (Q8+Q8_heat)/2            # Use average quality for further calculations

    LH_H = HST_from_PQ(P_H, 1, Hfluid)[0] - HST_from_PQ(P_H, 0, Hfluid)[0]      # Specific latent heat of vaporisation of HTC fluid
    D_Hvap, V_Hvap = cp.PropsSI(['D', 'V'], 'P', P_H, 'Q', 1, Hfluid)
    D_Hliq, V_Hliq, L_Hliq, I_Hliq, C_Hliq = cp.PropsSI(['D', 'V', 'L', 'I', 'C'], 'P', P_H, 'Q', 0, Hfluid)
    h_H_R1 = Chen_Bennett(m=mdot_H, x=Q_H_R1, D=d_pipe, rhol=D_Hliq, rhog=D_Hvap, mul=V_Hliq, mug=V_Hvap, kl=L_Hliq, Cpl=C_Hliq, Hvap=LH_H, sigma=I_Hliq, dPsat=0, Te=0)
    # Found convective heat transfer coefficient on HTC side!
    # print('Convective heat transfer coefficient on HTC side =',str(h_H_R1),'W/(m^2 K)')

    U_R1 = (h_L_R1*h_H_R1)/(h_L_R1+h_H_R1)                  # Found overall heat transfer coefficient in Region 1!
    # print('Thus, overall heat transfer coefficient in Region 1 =',str(U_R1),'W/(m^2 K)')
    LMTD_R1 = ((T2-T_H) - (T3-T_H))/math.log((T2-T_H)/(T3-T_H))
    # print('LMTD in Region 1 =',str(LMTD_R1),'K')
    area_R1 = Qdot_R1/(U_R1*LMTD_R1)
    # print('Area obtained for Region 1 =',str(area_R1),'m^2')

    results_R1 = pd.DataFrame([['Rate of HT in Region 1 (W)', Qdot_R1],
                               ['Convective HT coefficient on LTC side (W/m^2 K)', h_L_R1],
                               ['Convective HT coefficient on HTC side (W/m^2 K)', h_H_R1],     
                               ['Overall HT coefficient (W/m^2 K)', U_R1],
                               ['Logarithmic mean temperature difference (K)', LMTD_R1],
                               ['Thus, total area of Region 1 (m^2)', area_R1]], columns=['Parameter', 'Value'])
    results_R1.index += 1
    print(results_R1)

    area_NET += area_R1

    # Region 2: LTC mixture, HTC mixture
    print('\nRegion 2: LTC fluid is a mixture, HTC fluid is a mixture')
    # Pressure in LTC stays at P2, Temperature stays at T3
    h3 = streams['h'][3]                            # Specific enthalpy of LTC fluid at Region 2 outlet
    Qdot_R2 = mdot_L*(h2_cool-h3)
    # print('Rate of heat transfer in Region 2 =',str(Qdot_R2),'W')
    Q_L_R2 = (1+0)/2            # Use average quality for further calculations
    
    LH_L = HST_from_PQ(P_L, 1, Lfluid)[0] - HST_from_PQ(P_L, 0, Lfluid)[0]      # Specific latent heat of vaporisation of LTC fluid
    D_Lvap, V_Lvap = cp.PropsSI(['D', 'V'], 'P', P_L, 'Q', 1, Lfluid)
    D_Lliq, V_Lliq, L_Lliq, I_Lliq, C_Lliq = cp.PropsSI(['D', 'V', 'L', 'I', 'C'], 'P', P_L, 'Q', 0, Lfluid)
    h_L_R2 = Chen_Bennett(m=mdot_L, x=Q_L_R2, D=d_pipe, rhol=D_Lliq, rhog=D_Lvap, mul=V_Lliq, mug=V_Lvap, kl=L_Lliq, Cpl=C_Lliq, Hvap=LH_L, sigma=I_Lliq, dPsat=0, Te=0)
    # Found convective heat transfer coefficient on LTC side!
    # print('Convective heat transfer coefficient on LTC side =',str(h_L_R2),'W/(m^2 K)')

    Q_H_R2 = (Q8_heat+1)/2
    h_H_R2 = Chen_Bennett(m=mdot_H, x=Q_H_R2, D=d_pipe, rhol=D_Hliq, rhog=D_Hvap, mul=V_Hliq, mug=V_Hvap, kl=L_Hliq, Cpl=C_Hliq, Hvap=LH_H, sigma=I_Hliq, dPsat=0, Te=0)
    # Found convective heat transfer coefficient on HTC side!
    # print('Convective heat transfer coefficient on HTC side =',str(h_H_R2),'W/(m^2 K)')

    U_R2 = (h_L_R2*h_H_R2)/(h_L_R2+h_H_R2)                  # Found overall heat transfer coefficient in Region 1!
    # print('Thus, overall heat transfer coefficient in Region 1 =',str(U_R2),'W/(m^2 K)')
    LMTD_R2 = 5                 # Simple phase change process, both temperature profiles are flat and parallel
    # print('LMTD in Region 1 =',str(LMTD_R2),'K')
    area_R2 = Qdot_R2/(U_R2*LMTD_R2)
    # print('Area obtained for Region 1 =',str(area_R2),'m^2')

    results_R2 = pd.DataFrame([['Rate of HT in Region 2 (W)', Qdot_R2],
                               ['Convective HT coefficient on LTC side (W/m^2 K)', h_L_R2],
                               ['Convective HT coefficient on HTC side (W/m^2 K)', h_H_R2],     
                               ['Overall HT coefficient (W/m^2 K)', U_R2],
                               ['Logarithmic mean temperature difference (K)', LMTD_R2],
                               ['Thus, total area of Region 2 (m^2)', area_R2]], columns=['Parameter', 'Value'])
    results_R2.index += 1
    print(results_R2)

    area_NET += area_R2
    
    print('\nModelling complete. Total area required =',str(area_NET),'m^2')
    return None