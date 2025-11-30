import pandas as pd
import matplotlib.pyplot as plt

def plot_altitude_vs_aging(csv_path="worldcities_time_dilation.csv"):
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(10, 6))
    plt.scatter(df["altitude_m"], df["microseconds_difference_per_year"], alpha=0.4)

    plt.xlabel("Altitude (meters)")
    plt.ylabel("Microseconds Gained/Lost per Year")
    plt.title("Effect of Altitude on Aging Rate (Relativistic Time Dilation)")
    plt.grid(True)
    plt.show()


def plot_latitude_vs_aging(csv_path="worldcities_time_dilation.csv"):
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(10, 6))
    plt.scatter(df["lat"], df["microseconds_difference_per_year"], alpha=0.4)

    plt.xlabel("Latitude (degrees)")
    plt.ylabel("Microseconds Gained/Lost per Year")
    plt.title("Effect of Earth's Rotation (Latitude) on Aging Rate")
    plt.grid(True)
    plt.show()
