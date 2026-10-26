import numpy as np;
import matplotlib.pyplot as plt
from constraint_figure import constraintDiagram

# Constants
g = 32.2
rho = 0.002372

# Current Iteration Constraints
ground_roll = 120 #ft
turn_radius = 100 #ft 
stall_max = 48 #ft/s
altitude = 80 #ft
cruise_speed = 80 #ft/s
climb_hdist = 300 # ft

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

AR = 5.0
WS = np.linspace(0.5,4.0,num=351, endpoint=True)

TW_cruise_vals = TW_cruise(WS,AR,cruise_speed)
TW_g = TW_ground(WS,ground_roll)
TW_climb = TW_climb_angle(AR,climb_hdist,altitude)
TW_turn_vals = TW_levelturn(WS,AR,cruise_speed, turn_radius)
WS_s = WS_stall(stall_max)

constraintDiagram(TW_cruise_vals, TW_turn_vals, TW_g, TW_climb, WS, WS_s, AR)


# plt.plot(WS, TW_cruise_vals, label="Cruise at 80 ft/s")
# plt.plot(WS, TW_turn_vals, label="Turning (R = 100 ft)")
# plt.plot(WS, TW_g, label="Ground Roll (100 ft)")
# plt.axvline(x=WS_s, color='red', label='Max Stall Line')
# plt.axhline(y=TW_climb, color='red', label="Climb Angle" )
# plt.ylabel("Thrust to Weight Ratio (T/W)")
# plt.xlabel("Wing Loading (W/S; lb/ft^2)")
# plt.plot(3.1,0.4, 'rd', label="Design Point")
# plt.title(f"T/W and Wingloading Constraint Diagram (AR = {AR})")
# plt.legend()
# plt.show()





