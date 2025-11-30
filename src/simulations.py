import numpy as np
import matplotlib.pyplot as plt
from src.physics import time_dilation_sequence

def simulation_time_dilation(total_time=10, velocity=0.8 * 299_792_458):
    """
    total_time: seconds
    velocity: meters per second
    Note: Multiply velocity fraction by speed of light!
    """
    t, tau = time_dilation_sequence(total_time, velocity)
    return {
        "coordinate_time": t,
        "proper_time": tau
    }

def simulation_brain_sampling(total_time=2.0, real_fps=1000, brain_fps=20):
    real_time = np.linspace(0, total_time, int(real_fps * total_time))

    # brain perceives discrete frames
    brain_interval = 1.0 / brain_fps
    perceived_time = np.arange(0, total_time, brain_interval)

    return {
        "real_time": real_time,
        "perceived_time": perceived_time
    }

def simulation_spacetime(total_time=10, velocity=0.8):
    """
    Simulate spacetime worldlines for a stationary and moving observer.
    """
    c = 1.0
    t = np.linspace(0, total_time, 500)

    # Stationary observer
    x_stationary = np.zeros_like(t)
    proper_time_stationary = t   # same as coordinate time

    # Moving observer
    x_moving = velocity * t
    gamma = 1.0 / np.sqrt(1 - velocity**2 / c**2)
    proper_time_moving = t / gamma

    return {
        "t": t,
        "x_stationary": x_stationary,
        "x_moving": x_moving,
        "proper_time_stationary": proper_time_stationary,
        "proper_time_moving": proper_time_moving
    }

def spacetime_ticks(t, proper_time, num_ticks=10):
    """
    Generate tick marks for proper time along each worldline.
    """
    max_proper = proper_time[-1]
    tick_values = np.linspace(0, max_proper, num_ticks)

    tick_indices = [np.abs(proper_time - tv).argmin() for tv in tick_values]
    tick_times = t[tick_indices]

    return tick_times, tick_indices

def simulation_3d_worldline(total_time=5, velocity=0.5):
    """
    Generate a 3D spacetime worldline:
    x(t), y(t)=0, t
    """
    t = np.linspace(0, total_time, 500)

    # spatial motion
    x = velocity * t
    y = np.zeros_like(t)

    return {"t": t, "x": x, "y": y}
