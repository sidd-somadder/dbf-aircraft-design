import numpy as np;

# Constants
g = 32.2
rho = 0.002372

# Current Iteration Constraints
ground_roll = 100 #ft
turn_radius = 100 #ft 
stall_max = 48 #ft/s
altitude = 80 #ft
cruise_speed = 80 #ft/s

# Estimated performance values
CD_min = 0.04
CL_to = 0.7
CD_to = 0.07
CL_max = 1.3
mu_GR = 0.04
e = 0.70

def TW_cruise(WS,AR,V_cr):
    k = 1/(np.pi * e * AR)
    q = (1/2)*rho*(V_cr**2)
    return q*CD_min*(1/WS) + (k/q)*WS

def TW_ground(WS,ground_roll):
    term1 = (1.21/(g*rho*CL_max*ground_roll))*WS
    term2 = (0.605/CL_max)*(CD_to - mu_GR*CL_to)
    return term1 + term2 + mu_GR

def TW_levelturn(WS,AR,V_cr,turn_radius):
    theta = np.arctan((V_cr**2)/(turn_radius*g))
    load_fac = 1/np.cos(theta)
    k = 1/(np.pi * e * AR)
    q = (1/2)*rho*(V_cr**2)
    return q*((CD_min/WS) + k*((load_fac/q)**2)*WS)

def WS_stall(V_s):
    return 0.5*rho* V_s**2 * CL_max

def TW_climb_angle(AR, climb_dist, altitude):
    k = 1/(np.pi * e * AR)
    gamma = np.arctan(altitude / climb_dist)
    return np.sin(gamma) + np.sqrt(4 * k * CD_min)






