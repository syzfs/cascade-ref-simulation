from shorthands import *
import math
import pandas as pd

def compute_area(streams, T_overlap, Hfluid, Lfluid, d_hyd):
    area_CHX = 0                    # Initialise the summation term

    # Region 1: LTC gas, HTC mixture
    # Pressure in LTC stays at P2, throughout the CHX
    mdot_L = streams['mdot'][2]
    P_L = streams['P'][2]
    h2 = streams['h'][2]                            # Specific enthalpy of LTC fluid at the Region 1 left endpoint
    h2_cool = HST_from_PQ(P_L, 1, Lfluid)[0]        # Specific enthalpy of LTC fluid at the Region 1 right endpoint
    Qdot_R1 = mdot_L*(h2-h2_cool)
    # Found rate of heat transfer in Region 1!

    T2 = streams['T'][2]
    T3 = streams['T'][3]
    T_L = (T2+T3)/2              # Take average of T2 and T2cool (which is equal to T3)
    Nu_L = 615.27                # Representative value from the correlation
    h_L_R1 = Nu_L*cp.PropsSI('L', 'T', 275.5, 'P', P_L, Lfluid)/d_hyd    # k=0.013
    # Found convective heat transfer coefficient on LTC side!

    P_H = streams['P'][5]        # Pressure stays at P5, throughout Region 1
    T_H = streams['T'][5]        # Temperature stays at T5
    mdot_H = streams['mdot'][5]
    h5 = streams['h'][5]                            # Specific enthalpy of HTC fluid at the Region 1 left endpoint
    h8_heat = h5 - (Qdot_R1/mdot_H)                 # Specific enthalpy of HTC fluid at the Region 1 right endpoint
    Q5 = streams['Q'][5]                            # Quality of HTC fluid at Region 1 left endpoint
    Q8_heat = Q_from_PH(P_H, h8_heat, Hfluid)       # Quality of HTC fluid at Region 1 right endpoint
    Q_H_R1 = (Q5+Q8_heat)/2      # Use average quality for further calculations. Equal to 0.78
    h_H_R1 = 5375                # Representative value from the graph
    # Found convective heat transfer coefficient on HTC side!

    U_R1 = (h_L_R1*h_H_R1)/(h_L_R1+h_H_R1)
    # Found overall heat transfer coefficient for Region 1!
    LMTD_R1 = ((T2-T_H) - (T3-T_H))/math.log((T2-T_H)/(T3-T_H))
    # Found LMTD for Region 1!  
    area_R1 = Qdot_R1/(U_R1*LMTD_R1)
    # Found area required for Region 1!

    results_R1 = pd.DataFrame([['Rate of HT in Region 1 (W)', round(Qdot_R1,3)],
                              #  ['Convective HT coefficient on LTC side (W/m^2 K)', h_L_R1],
                              #  ['Convective HT coefficient on HTC side (W/m^2 K)', h_H_R1],     
                               ['Overall HT coefficient (W/m^2 K)', round(U_R1,3)],
                               ['Logarithmic mean temperature difference (K)', round(LMTD_R1,3)],
                               ['Thus, total area of Region 1 (m^2)', round(area_R1,3)]], columns=['Parameter', 'Value'])
    results_R1.index += 1
    # Stored results of Region 1

    area_CHX += area_R1

    # Region 2: LTC mixture, HTC mixture
    # Pressure in LTC stays at P2, Temperature stays at T3
    h3 = streams['h'][3]            # Specific enthalpy of LTC fluid at Region 2 right endpoint
    Qdot_R2 = mdot_L*(h2_cool-h3)
    # Found rate of heat transfer in Region 2!
    
    Q_L_R2 = (1+0)/2                # Use average quality for further calculations. Equal to 0.5
    h_L_R2 = 6250                   # Representative value from graph
    # Found convective heat transfer coefficient on LTC side!

    Q8 = streams['Q'][8]
    Q_H_R2 = (Q8_heat+Q8)/2         # Equal to approximately 0.5
    h_H_R2 = 6250                   # Representative value from graph
    # Found convective heat transfer coefficient on HTC side!

    U_R2 = (h_L_R2*h_H_R2)/(h_L_R2+h_H_R2)
    # Found overall heat transfer coefficient for Region 2!
    LMTD_R2 = T_overlap         # Simple phase change process, both temperature profiles are flat and parallel
    # Found LMTD for Region 2!
    area_R2 = Qdot_R2/(U_R2*LMTD_R2)
    # Found area required for Region 2!

    results_R2 = pd.DataFrame([['Rate of HT in Region 2 (W)', round(Qdot_R2,3)],
                            #    ['Convective HT coefficient on LTC side (W/m^2 K)', h_L_R2],
                            #    ['Convective HT coefficient on HTC side (W/m^2 K)', h_H_R2],     
                               ['Overall HT coefficient (W/m^2 K)', round(U_R2,3)],
                               ['Logarithmic mean temperature difference (K)', round(LMTD_R2,3)],
                               ['Thus, total area of Region 2 (m^2)', round(area_R2,3)]], columns=['Parameter', 'Value'])
    results_R2.index += 1
    # Stored results for Region 2!

    area_CHX += area_R2
    # Found total area for the entire CHX!
    return results_R1, results_R2, area_CHX