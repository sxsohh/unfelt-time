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
