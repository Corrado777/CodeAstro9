import numpy as np
import matplotlib.pyplot as plt

def plot_ephemeris(timepoints, altitudes_mars, altitudes_earth, target_str):
    """
    Plots the ephemeris of Mars.

    Parameters:
    timepoints (list): List of timepoints.
    altitudes (list): List of altitudes corresponding to the timepoints.

    Returns:
    None
    """

    plt.plot(timepoints, altitudes_mars, label='Mars')
    plt.plot(timepoints, altitudes_earth, label='Earth')
    plt.title(f'{target_str} Ephemeris on Mars/Earth at Given Observatory')
    plt.xlabel('Time (Julian Date)')
    plt.ylabel('Altitude [deg]')
    plt.legend()
    plt.show()

