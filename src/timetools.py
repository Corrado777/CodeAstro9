from astropy.time import Time

def get_julian_date(earth_time):
    # Convert Earth time to Julian Date
    earth_time_astropy = Time(earth_time, format='iso', scale='utc')
    return earth_time_astropy.jd

