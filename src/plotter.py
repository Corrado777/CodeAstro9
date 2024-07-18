import numpy as np
import matplotlib.pyplot as plt

def plot_ephemeris(timepoints, altitudes, target_str):
    """
    Plots the ephemeris of Mars.

    Parameters:
    timepoints (list): List of timepoints.
    altitudes (list): List of altitudes corresponding to the timepoints.

    Returns:
    None
    """

    plt.plot(timepoints, altitudes, label=target_str)
    plt.title(f'{target_str} Ephemeris on Mars at Given Observatory')
    plt.xlabel('Time (Julian Date)')
    plt.ylabel('Altitude [deg]')
    plt.legend()
    plt.show()

