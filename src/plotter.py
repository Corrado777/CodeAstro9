import numpy as np
import matplotlib.pyplot as plt

def plot_ephemeris(timepoints, altitudes):

    plt.plot(timepoints, altitudes, label='Mars')
    plt.xlabel('Time')
    plt.ylabel('Altitude [deg]')
    plt.legend()
    plt.show()