import numpy as np
import matplotlib.pyplot as plt

def plot_ephemeris(altitudes, date, time, period, save = False):
    '''
    Plots the ephemeris of a celestial object based on its altitude over time.

    Parameters:
    -----------
    altitudes : array-like
        A sequence of altitude values to plot.
    date : str
        The date for which the ephemeris is plotted, formatted as 'YYYY-MM-DD'.
    time : float
        The current time in hours.
    period : float
        The period over which the ephemeris is plotted, in hours.
    save : bool, optional
        If True, the plot will be saved as a PNG file with the name 'ephemeris_<date>.png'.
        Default is False.

    Returns:
    --------
    None
    '''
    
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_title(f'Ephemeris for {date}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Altitude')

    # Timepoints centered on date and time, half a period in each direction
    timepoints = np.linspace(time - period/2, time + period/2, 100)

    # Plot the ephemeris
    ax.plot(timepoints, altitudes, label='Altitude')
    ax.axvline(time, color='red', linestyle='--', label='Current time')
    ax.legend()
    ax.grid()
    plt.show()

    if save:
        fig.savefig(f'ephemeris_{date}.png')


if __name__ == '__main__':
    altitudes = np.sin(np.linspace(0, 2*np.pi, 100))
    date = '2021-01-01'
    time = 12
    period = 24
    plot_ephemeris(altitudes, date, time, period, save=False)

