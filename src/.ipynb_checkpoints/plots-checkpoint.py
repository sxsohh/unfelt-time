import matplotlib.pyplot as plt

def plot_time_dilation(coordinate_time, proper_time):
    plt.figure(figsize=(8, 6))
    plt.plot(coordinate_time, proper_time, label='Proper Time (Observer Moving)')
    plt.plot(coordinate_time, coordinate_time, label='Coordinate Time (Stationary)')
    plt.xlabel("Coordinate Time")
    plt.ylabel("Time Experienced")
    plt.legend()
    plt.title("Time Dilation: Proper Time vs Coordinate Time")
    plt.grid(True)
    plt.show()
