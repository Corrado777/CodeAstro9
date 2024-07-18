import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Longitude
from astropy import units as u

import src as src
import src.observatory
import src.planet
import src.Load_item
import src.timetools
import src.calc_pos
import src.plotter




def scale_julian_date(julian_date):
    # Mars' sidereal period in days
    mars_sidereal_period = 1.027491
    
    # Convert Julian Date to Astropy Time object
    # time = Time(julian_date, format='jd')
    
    # Calculate the fraction of a day since a known Mars LST epoch (JD)
    jd_since_epoch = julian_date - 2451549.5 # - 0.00886519
    mars_jd_equivilent = jd_since_epoch / mars_sidereal_period
    
    return mars_jd_equivilent

def get_mars_sky_coords(julian_date, mars_location_longitude, mars_location_latitude, target_str):
    # Calculate Local Sidereal Time (LST) for the given Mars location and time
    mars_jd = scale_julian_date(julian_date)
    
    # Assuming you have the longitude and latitude for your observation point on Mars
    mars_location = EarthLocation(lat=mars_location_latitude*u.deg, lon=mars_location_longitude*u.deg, height=0*u.m)
    
    # Convert to AltAz frame at the given LST and location on Mars
    altaz = AltAz(obstime=Time(mars_jd, format='jd'), location=mars_location)
    
    # Example: Get the sky position of Sirius
    target = SkyCoord.from_name(target_str)
    target_altaz = target.transform_to(altaz)
    
    #print(f"targets's position on Mars at jd {julian_date}: Altitude {sirius_altaz.alt}, Azimuth {sirius_altaz.az}")
    return target_altaz.alt.value

def get_earth_sky_coords(julian_date, earth_location_longitude, earth_location_latitude, target_str):
    
    
    # Assuming you have the longitude and latitude for your observation point on Mars
    earth_location = EarthLocation(lat=earth_location_latitude*u.deg, lon=earth_location_longitude*u.deg, height=0*u.m)
    
    # Convert to AltAz frame at the given LST and location on Mars
    altaz = AltAz(obstime=Time(julian_date- 2451549.5, format='jd'), location=earth_location)
    
    # Example: Get the sky position of Sirius
    target = SkyCoord.from_name(target_str)
    target_altaz = target.transform_to(altaz)
    
    #print(f"Target's position on Mars at jd {julian_date}: Altitude {sirius_altaz.alt}, Azimuth {sirius_altaz.az}")
    return target_altaz.alt.value





def main():
    print("Welcome to Martian Star Hunter!")
    print("""
        *
  *       *
       ___ 
      / o \\
     /     \\
  __/_______\\__
 /_____________\\
/_______________\\
  _____|_____
/             \\
|_____________|

     Mars Observatory
""")


    '''User Inputs'''

    planet_name = input("Enter the name of the planet where the observatory will be located: ")
    assert planet_name =='Mars', 'The planet name is not Mars, please enter the correct planet name'


    # Prompt the user to enter observatory latitude and Longitude
    location = input("Enter observatory latitude and longitude separated by commas (e.g., value1,value2): ")


    date_string = input("Enter the date in the format YYYY-MM-DD: ")


    target_name = input("Enter the name of the target object: ")
    assert type(target_name) == str, 'The target name is not a string, please enter the correct target name'


    '''End of User Inputs. '''

    # Convert the input string to a tuple by splitting the string and then using tuple() to convert the list to a tuple
    latitude, longitude = tuple(location.split(','))
    latitude = float(latitude)
    longitude = float(longitude)

    
    # initialize a new observatory object with the latitude and longitude
    observatory = src.observatory.Observatory(planet_name, latitude, longitude)

    # initialize a new planet object
    planet = src.planet.Planet()
    planet_data = src.Load_item.load_planet(planet_name, date_string)
    

    planet.ra = planet_data['RA'] # planet location on celestial sphere as seen from Earth
    planet.dec = planet_data['DEC']
    planet.period = planet_data['SIDEREAL_ROT_PERIOD']
    planet.distance = planet_data['EARTHRANGE']
    planet.radius = planet_data['VOL_MEAN_RADIUS']
    planet.tilt = planet_data['OBLIQUITY TO ORBIT']
    planet.label = planet_data['NAME']


    # Get the Julian date of the observation date
    julian_date = src.timetools.get_julian_date(date_string)

    # Get the position of the target with respect to the observatory/planet in degrees
    rel_position = src.calc_pos.calc_pos_target_rel_planet(planet, target_name)

    # Get the altitude of the target on the maritan sky where the observatory is
    # mars_altitude = get_mars_sky_coords(julian_date, observatory.longitude, observatory.latitude, target_name)
    # print(f"The altitude of {target_name} on the Martian sky is: {mars_altitude} degrees")

    timepoints = Time(julian_date, format='jd') + np.linspace(-0.5, 0.5, 500)
    mars_alt = []
    for time in timepoints:
        mars_alt.append(get_mars_sky_coords(time.jd, observatory.longitude, observatory.latitude, target_name))
    
    src.plotter.plot_ephemeris(timepoints.value, mars_alt, target_name)




if __name__ == '__main__':
    main()