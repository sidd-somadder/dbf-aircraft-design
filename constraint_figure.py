import numpy as np
import matplotlib.pyplot as plt

# Current Iteration Constraints
ground_roll = 120 #ft
turn_radius = 100 #ft 
stall_max = 48 #ft/s
altitude = 80 #ft
cruise_speed = 80 #ft/s
climb_hdist = 300 # ft

C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]   # cruise, turn, takeoff, climb
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "serif", "font.size": 10})

def constraintDiagram(TW_cruise, TW_turn, TW_g, TW_climb, WS, WS_s, AR):
    fig, ax = plt.subplots(figsize=(6.5, 4.3), dpi=150)

    # Feasible region: left of the stall line and above every T/W curve
    upper = np.maximum.reduce([TW_cruise, TW_turn, TW_g,
                            np.full_like(WS, TW_climb)])
    ax.fill_between(WS, upper, 0.7, where=WS <= WS_s, color=C[2], alpha=0.10,
                    linewidth=0, label="Feasible region")

    ax.plot(WS, TW_cruise, color=C[0], lw=2, label=f"Cruise ({cruise_speed} ft/s)")
    ax.plot(WS, TW_turn, color=C[1], lw=2, ls=(0, (6, 2)),
            label=f"Level turn (R = {turn_radius} ft)")
    ax.plot(WS, TW_g, color=C[2], lw=2, ls=(0, (2, 2)),
            label=f"Takeoff ({ground_roll} ft ground roll)")
    ax.axhline(TW_climb, color=C[3], lw=2, ls=(0, (8, 2, 2, 2)),
            label=f"Climb ({altitude} ft over {climb_hdist} ft)")
    ax.axvline(WS_s, color=INK2, lw=1.5, label=f"Stall limit ({stall_max} ft/s)")

    # Design point
    ax.plot(3.1, 0.4, marker="o", ms=8, ls="none", color=INK, mec="white", mew=2,
            zorder=5, label="Design point")

    ax.set_xlim(WS[0], WS[-1])
    ax.set_ylim(0.1, 0.7)
    ax.set_xlabel(r"Wing loading $W/S$ (lb/ft$^2$)")
    ax.set_ylabel(r"Thrust-to-weight ratio $T/W$")
    ax.set_title(f"T/W and Wing Loading Constraint Diagram (AR = {AR})")
    ax.grid( lw=0.6)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
    ax.tick_params(colors=INK2)
    ax.legend(loc="upper right", fontsize=8, frameon=True, framealpha=0.95, edgecolor=GRID)

    fig.tight_layout()
    plt.show()