import CoolProp.CoolProp as cp

# Super / Sub:
def HS_from_TP(t, p, fluid):
    h, s = cp.PropsSI(['H', 'S'], 'T', t, 'P', p, fluid)
    return h, s

def ST_from_PH(p, h, fluid):
    s, t = cp.PropsSI(['S', 'T'], 'P', p, 'H', h, fluid)
    return s, t

def TP_from_HS(h, s, fluid):
    t, p = cp.PropsSI(['T', 'P'], 'H', h, 'S', s, fluid)
    return t, p

def PH_from_ST(s, t, fluid):
    p, h = cp.PropsSI(['P', 'H'], 'S', s, 'T', t, fluid)
    return p, h

def HT_from_PS(p, s, fluid):
    h, t = cp.PropsSI(['H', 'T'], 'P', p, 'S', s, fluid)
    return h, t

def PS_from_TH(t, h, fluid):
    p, s = cp.PropsSI(['P', 'S'], 'T', t, 'H', h, fluid)
    return p, s
# #####

# Saturation Dome:
# Quality Known:
def HST_from_PQ(p, q, fluid):
    h, s, t = cp.PropsSI(['H', 'S', 'T'], 'P', p, 'Q', q, fluid)
    return h, s, t

def STP_from_HQ(h, q, fluid):
    s, t, p = cp.PropsSI(['S', 'T', 'P'], 'H', h, 'Q', q, fluid)
    return s, t, p

def TPH_from_SQ(s, q, fluid):
    t, p, h = cp.PropsSI(['T', 'P', 'H'], 'S', s, 'Q', q, fluid)
    return t, p, h

def PHS_from_TQ(t, q, fluid):
    p, h, s = cp.PropsSI(['P', 'H', 'S'], 'T', t, 'Q', q, fluid)
    return p, h, s

# Quality Unknown:
def Q_from_PH(p, h, fluid):
    q = cp.PropsSI('Q', 'P', p, 'H', h, fluid)
    return q

# Write 5 more (not 6, because ..._from_PT() is useless)
# ...or maybe not needed
# #####