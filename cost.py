import pandas as pd

# Get simulation outputs, find costs
def capital(streams, results, area_CHX, area_HTCC, area_LTCE):      # For CHX, we may have to add more input parameters to compute c_CHX
    ci_ratio_22by19 = 331/289
    ci_ratio_22by15 = 331/254
    # LTC Compressor: Use cost indices on 2019 cost function
    c_compL = 959791.6*((results.iloc[0,1]/1000)**0.46) * ci_ratio_22by19
    # LTC EV: Use cost indices on 2019 cost function
    c_evL = 10808.6*(streams['mdot'][3]) * ci_ratio_22by19
    # LTC Evaporator: Use cost indices on 2019 cost function
    c_evapL = 131874.0*(area_LTCE**0.89) * ci_ratio_22by19

    # CHX: Use cost indices on 2015 cost function
    c_CHX = 56380.5*(area_CHX**0.8) * ci_ratio_22by15

    # HTC Compressor: Use cost indices on 2019 cost function
    c_compH = 959791.6*((results.iloc[1,1]/1000)**0.46) * ci_ratio_22by19
    # HTC EV: Use cost indices on 2019 cost function
    c_evH = 10808.6*(streams['mdot'][7]) * ci_ratio_22by19
    # HTC Condenser: Use cost indices on 2019 cost function
    c_condH = 131874.0*(area_HTCC**0.89) * ci_ratio_22by19

    # Total
    c_results = pd.DataFrame([['LTC Compressor', round(c_compL,2)],
                              ['LTC Throttle Valve', round(c_evL,2)],
                              ['LTC Evaporator', round(c_evapL,2)],
                              ['Cascade Heat Exchanger', round(c_CHX,2)],
                              ['HTC Compressor', round(c_compH,2)],
                              ['HTC Throttle Valve', round(c_evH,2)],
                              ['HTC Condenser', round(c_condH,2)]], columns=['Component', 'Price in ₹ (2022)'])
    c_results.index += 1
    c_TOT = c_compL+c_evL+c_evapL+c_CHX+c_compH+c_evH+c_condH
    return c_results, c_TOT