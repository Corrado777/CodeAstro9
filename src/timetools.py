from astropy.time import Time
import datetime
from astropy.coordinates import get_sun, AltAz, solar_system_ephemeris


class TimeConverter:
    def __init__(self, earth_date, earth_time):
        self.earth_date = earth_date
        self.earth_time = earth_time

        # Constants based on Earth and Mars day lengths
        self.earth_day_seconds = 24 * 60 * 60  # seconds in an Earth day
        self.mars_day_seconds = 24.6597 * 60 * 60  # seconds in a Mars day

    def convert_to_mars_time(self):
        '''
        Converts Earth date and time to Martian time.

        This method converts Earth date and time to Martian years, sols (Martian days), 
        and the corresponding hours, minutes, and seconds on Mars.

        Returns:
        --------
        tuple
            A tuple containing the Martian time components:
            - Mars years (float)
            - Mars sols (float)
            - Mars hours (int)
            - Mars minutes (int)
            - Mars seconds (int)

        Notes:
        ------
        - The reference epoch for Earth time is March 12, 1609.
        - One Martian sol is approximately 88775.244 seconds.
        - One Martian year is approximately 669.6 sols.
        '''

        # Extract Earth time components
        earth_hours, earth_minutes, earth_seconds = self.earth_time

        # Convert Earth date and time to total seconds since the beginning of epoch (for simplicity)
        earth_total_seconds = (self.earth_date - datetime.datetime(1609, 3, 12)).total_seconds() \
                              + earth_hours * 3600 + earth_minutes * 60 + earth_seconds

        # Calculate Mars time in sols (Martian days)
        mars_sols = earth_total_seconds / self.mars_day_seconds

        # Calculate Mars time in years
        mars_years = mars_sols / 669.6

        # Convert remaining seconds to Martian time
        mars_seconds = earth_total_seconds % self.mars_day_seconds
        mars_hours = mars_seconds // 3600
        mars_seconds %= 3600
        mars_minutes = mars_seconds // 60
        mars_seconds %= 60

        return mars_years, mars_sols, int(mars_hours), int(mars_minutes), int(mars_seconds)

    def get_sun_position_on_mars(self, mars_location):
        '''
        Calculates the Sun's position (altitude and azimuth) from a specified location on Mars at a given Earth date and time.

        Parameters:
        -----------
        mars_location : `astropy.coordinates.EarthLocation`
            The location on Mars for which to calculate the Sun's position.

        Returns:
        --------
        tuple
            A tuple containing the Sun's altitude and azimuth in degrees at the specified Mars location.

        Notes:
        ------
        - This method uses the solar system ephemeris to calculate the Sun's position.
        - The `mars_location` should be provided as an `EarthLocation` object with appropriate Mars coordinates.
        '''
        # Create a Time object for the given Earth date and time
        time = Time(self.earth_date + datetime.timedelta(hours=self.earth_time[0], minutes=self.earth_time[1], seconds=self.earth_time[2]))

        # Use the solar system ephemeris to calculate the Sun's position
        with solar_system_ephemeris.set('builtin'):
            mars = get_body('mars', time)
            sun = get_sun(time)

        # Transform Sun's position to the local AltAz frame on Mars
        altaz = AltAz(obstime=time, location=mars_location)
        sun_altaz = sun.transform_to(altaz)

        return sun_altaz.alt, sun_altaz.az




def get_julian_date(earth_time):
    '''
    Converts Earth time to Julian Date.

    Parameters:
    -----------
    earth_time : str
        The Earth time in ISO format (e.g., 'YYYY-MM-DD HH:MM:SS').

    Returns:
    --------
    float
        The corresponding Julian Date.
    '''

    # Convert Earth time to Julian Date
    earth_time_astropy = Time(earth_time, format='iso', scale='utc')
    return earth_time_astropy.jd

