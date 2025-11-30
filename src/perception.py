import numpy as np

def subjective_time_sampling(real_time, sampling_rate=20):
    """
    Humans sample reality at about 20 Hz.
    Converts real time (continuous) into subjective time (discrete).
    """
    interval = 1 / sampling_rate
    subjective_ticks = np.arange(0, real_time[-1], interval)
    return subjective_ticks
