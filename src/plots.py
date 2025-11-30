import numpy as np
import matplotlib.pyplot as plt

def plot_time_dilation(coordinate_time, proper_time, save=False):
    plt.figure(figsize=(8, 6))

    # Both arrays should be same length now
    plt.plot(coordinate_time, proper_time, label="Proper Time (Moving Observer)")
    plt.plot(coordinate_time, coordinate_time, label="Coordinate Time (Stationary Observer)")

    plt.xlabel("Coordinate Time (t)")
    plt.ylabel("Experienced Time")
    plt.title("Time Dilation: Proper Time vs Coordinate Time")
    plt.grid(True)
    plt.legend()

    if save:
        plt.savefig("visuals/time_dilation.png", dpi=300)

    plt.show()

def plot_brain_sampling(real_time, perceived_time):
    plt.figure(figsize=(8, 6))
    plt.plot(real_time, np.zeros_like(real_time), label="Real Time", alpha=0.6)
    plt.scatter(perceived_time, np.zeros_like(perceived_time), color="red", label="Perceived Frames")
    plt.yticks([])
    plt.xlabel("Time (seconds)")
    plt.title("Brain Frame Sampling vs Reality")
    plt.legend()
    plt.grid()
    plt.show()


def plot_spacetime_diagram(t, x_stationary, x_moving):
    plt.figure(figsize=(7, 7))
    plt.plot(x_stationary, t, label="Stationary Observer", linewidth=2)
    plt.plot(x_moving, t, label="Moving Observer", linewidth=2)

    plt.xlabel("Space (x)")
    plt.ylabel("ct (time)")
    plt.title("Spacetime Diagram: Worldlines of Two Observers")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spacetime_with_ticks(t, x_stationary, x_moving,
                              ticks_stationary, ticks_moving,
                              idx_stationary, idx_moving):
    plt.figure(figsize=(8, 8))

    # Worldlines
    plt.plot(x_stationary, t, label="Stationary Observer", linewidth=2)
    plt.plot(x_moving, t, label="Moving Observer", linewidth=2)

    # Proper time ticks
    plt.scatter(x_stationary[idx_stationary], ticks_stationary,
                color="blue", s=40, label="Stationary Proper Time Ticks")
    plt.scatter(x_moving[idx_moving], ticks_moving,
                color="red", s=40, label="Moving Proper Time Ticks")

    plt.xlabel("Space (x)")
    plt.ylabel("ct (Time)")
    plt.title("Spacetime Diagram With Proper Time Ticks")
    plt.legend()
    plt.grid(True)
    plt.show()

from mpl_toolkits.mplot3d import Axes3D

def plot_3d_worldline(t, x, y):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, t, linewidth=2)

    ax.set_xlabel("Space X (light-seconds)")
    ax.set_ylabel("Space Y (light-seconds)")
    ax.set_zlabel("Time t (seconds)")

    ax.set_title("3D Spacetime Worldline")

    plt.show()
