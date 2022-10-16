import pandas as pd

# Get simulation outputs, find costs
def capital(streams, results, area_NET, evap_heatflux):      # For CHX, we may have to add more input parameters to compute c_CHX
    ci_ratio_22by19 = 331/289
    ci_ratio_22by15 = 331/254
    # LTC Compressor: Use cost indices on 2019 cost function
    c_compL = 959791.6*((results.iloc[0,1]/1000)**0.46) * ci_ratio_22by19
    # LTC EV: Use cost indices on 2019 cost function
    c_evL = 10808.6*(streams['mdot'][3]) * ci_ratio_22by19
    # LTC Evaporator: Use cost indices on 2019 cost function
    c_evapL = 131874.0*((results.iloc[3,1]/evap_heatflux)**0.89) * ci_ratio_22by19

    # CHX: Use cost indices on 2015 cost function
    c_CHX = 56380.5*(area_NET**0.8) * ci_ratio_22by15

    # HTC Compressor: Use cost indices on 2019 cost function
    c_compH = 959791.6*((results.iloc[1,1]/1000)**0.46) * ci_ratio_22by19
    # HTC EV: Use cost indices on 2019 cost function
    c_evH = 10808.6*(streams['mdot'][7]) * ci_ratio_22by19
    # HTC Condenser: Use cost indices on 2019 cost function
    c_condH = 131874.0*((results.iloc[4,1]/evap_heatflux)**0.89) * ci_ratio_22by19

    # Refrigerants: Assume we'll buy 50lbs i.e. 22.6796kg of R1234ze and 26.45lbs or 12kg of R23
    m_RefL = 12
    c_RefL = 2000*m_RefL        # Current prices (15/10/2022)
    m_RefH = 22.6796
    c_RefH = 8585.60*m_RefH     # Current prices (16/10/2022)

    # Total
    c_results = pd.DataFrame([['LTC Compressor', round(c_compL,2)],
                              ['LTC Throttle Valve', round(c_evL,2)],
                              ['LTC Evaporator', round(c_evapL,2)],
                              ['LTC Refrigerant', round(c_RefL,2)],
                              ['Cascade Heat Exchanger', round(c_CHX,2)],
                              ['HTC Compressor', round(c_compH,2)],
                              ['HTC Throttle Valve', round(c_evH,2)],
                              ['HTC Condenser', round(c_condH,2)],
                              ['HTC Refrigerant', round(c_RefH,2)]], columns=['Component', 'Price in ₹ (2022)'])
    c_results.index += 1
    c_TOT = c_compL+c_evL+c_evapL+c_RefL+c_CHX+c_compH+c_evH+c_condH+c_RefH
    return c_results, c_TOT