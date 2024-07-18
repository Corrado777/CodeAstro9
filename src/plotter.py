import numpy as np
import matplotlib.pyplot as plt

def plot_ephemeris(timepoints, altitudes):
    """
    Plots the ephemeris of Mars.

    Parameters:
    timepoints (list): List of timepoints.
    altitudes (list): List of altitudes corresponding to the timepoints.

    Returns:
    None
    """

    plt.plot(timepoints, altitudes, label='Mars')
    plt.xlabel('Time')
    plt.ylabel('Altitude [deg]')
    plt.legend()
    plt.show()

