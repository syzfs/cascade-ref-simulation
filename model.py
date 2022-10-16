from shorthands import *
import pandas as pd

def simulate(Hfluid, Lfluid, T1, T5, T_amb, T_gap, T_overlap, n_isH, n_isL, Q_ref, Q1, Q3, Q5, Q7):
    # Lower Temperature Cycle
    P5, h5, s5 = PHS_from_TQ(T5, Q5, Hfluid)
    P1, h1, s1 = PHS_from_TQ(T1, Q1, Lfluid)
    T3 = T5 + T_overlap
    P3, h3, s3 = PHS_from_TQ(T3, Q3, Lfluid) 
    P2 = P3
    h2s = cp.PropsSI('H', 'S', s1, 'P', P2, Lfluid)
    h2 = (h2s-h1)/n_isL + h1
    s2, T2 = ST_from_PH(P2, h2, Lfluid)
    h4 = h3
    P4 = P1
    s4, T4 = ST_from_PH(P4, h4, Lfluid)
    Q4 = Q_from_PH(P4, h4, Lfluid)

    # Higher Temperature Cycle
    T7 = T_amb + T_gap
    P7, h7, s7 = PHS_from_TQ(T7, Q7, Hfluid)
    P6 = P7
    h6s = cp.PropsSI('H', 'S', s5, 'P', P6, Hfluid)
    h6 = (h6s-h5)/n_isH + h5
    s6, T6 = ST_from_PH(P6, h6, Hfluid)
    h8 = h7
    P8 = P5
    s8, T8 = ST_from_PH(P8, h8, Hfluid)
    Q8 = Q_from_PH(P8, h8, Hfluid)

    # Mass Flow Rates, Performance, COPs
    mdotL = Q_ref/(h1-h4)
    mdotH = (h2-h3)*mdotL/(h5-h8)
    W_compL = mdotL*(h2-h1)
    W_compH = mdotH*(h6-h5)
    W_inNET = W_compH+W_compL
    Q_out = mdotH*(h6-h7)
    copL, copH = (h1-h4)/(h2-h1), (h5-h8)/(h6-h5)
    # copNET = (copL*copH)/(1+copL+copH)
    copNET = Q_ref/W_inNET

    # Compile
    streams = pd.DataFrame(columns=['h', 's', 'T', 'P', 'Q', 'mdot'])
    streams['h'] = [h1, h2, h3, h4, h5, h6, h7, h8]
    streams['s'] = [s1, s2, s3, s4, s5, s6, s7, s8]
    streams['T'] = [T1, T2, T3, T4, T5, T6, T7, T8]
    streams['P'] = [P1, P2, P3, P4, P5, P6, P7, P8]
    streams['Q'] = [Q1, '(superheated)', Q3, Q4, Q5, '(superheated)', Q7, Q8]
    streams['mdot'] = [mdotL, mdotL, mdotL, mdotL, mdotH, mdotH, mdotH, mdotH]
    streams.index += 1
    streams.index.rename('Stream', inplace=True)
    results = pd.DataFrame([['LTC work input (in W)', round(W_compL,3)],
                            ['HTC work input (in W)', round(W_compH,3)],
                            ['Total work input (in W)', round(W_inNET,2)],
                            ['Refrigeration effect (in W)', round(Q_ref,3)],
                            ['Heat rejection (in W)', round(Q_out,3)],
                            ['COP of LTC', round(copL,3)],
                            ['COP of HTC', round(copH,3)],
                            ['Overall COP', round(copNET,3)]], columns=['Parameter', 'Value'])
    results.index += 1
    # return streams, W_compL, W_compH, Q_out, copH, copL, copNET
    return streams, results