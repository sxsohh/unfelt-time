import sys, os
sys.path.append(os.path.abspath("src"))

from simulations import simulation_spacetime, spacetime_ticks
from plots import plot_spacetime_with_ticks

# Simulation
result = simulation_spacetime(total_time=10, velocity=0.8)

# Extract components
t = result["t"]
x_stat = result["x_stationary"]
x_mov = result["x_moving"]
tau_stat = result["proper_time_stationary"]
tau_mov = result["proper_time_moving"]

# Generate proper time ticks
ticks_stat, idx_stat = spacetime_ticks(t, tau_stat, num_ticks=10)
ticks_mov, idx_mov = spacetime_ticks(t, tau_mov, num_ticks=10)

# Plot
plot_spacetime_with_ticks(
    t,
    x_stat,
    x_mov,
    ticks_stat,
    ticks_mov,
    idx_stat,
    idx_mov
)
