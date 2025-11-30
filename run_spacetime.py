import sys, os
sys.path.append(os.path.abspath("src"))

from simulations import simulation_spacetime
from plots import plot_spacetime_diagram

result = simulation_spacetime(total_time=10, velocity=0.8)

plot_spacetime_diagram(
    result["t"],
    result["x_stationary"],
    result["x_moving"]
)
