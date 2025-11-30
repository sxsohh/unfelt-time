import sys, os
sys.path.append(os.path.abspath("src"))

from simulations import simulation_3d_worldline
from plots import plot_3d_worldline

result = simulation_3d_worldline(total_time=5, velocity=0.5)

plot_3d_worldline(
    result["t"],
    result["x"],
    result["y"]
)
