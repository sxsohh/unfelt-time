import numpy as np

c = 299_792_458  # speed of light in m/s

def proper_time_array(dt_array, velocity):
    """
    Compute proper time increments for each dt.
    dt_array: array of time deltas (length N)
    velocity: scalar velocity (m/s)
    Returns: array of same length as dt_array
    """
    gamma = np.sqrt(1 - (velocity**2) / c**2)
    return dt_array * gamma

def time_dilation_sequence(total_time, velocity, steps=1000):
    """
    Returns coordinate time array (t) and proper time array (tau),
    both length = steps
    """
    # coordinate time (0 to total_time)
    t = np.linspace(0, total_time, steps)

    # compute dt for each step
    dt = np.diff(t)               # length 999
    dt = np.insert(dt, 0, dt[0])  # make length 1000

    # compute proper time increments
    d_tau = proper_time_array(dt, velocity)  # length 1000

    # integrate
    tau = np.cumsum(d_tau)  # length 1000

    return t, tau
