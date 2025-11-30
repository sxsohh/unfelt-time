import sys
import os

sys.path.append(os.path.abspath("src"))

from simulations import simulation_brain_sampling
from plots import plot_brain_sampling

result = simulation_brain_sampling(total_time=2.0, real_fps=1000, brain_fps=20)

plot_brain_sampling(result["real_time"], result["perceived_time"])
