import numpy as np
import matplotlib.pyplot as plt

def plot_ephemeris(altitudes, date, time, period, save = False):

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

