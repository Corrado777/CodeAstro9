import src as src
import src.observatory
import src.planet
import src.Load_item
import src.timetools
import src.calc_pos

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

    print(latitude, longitude)  # This will print the tuple of values

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

    print("The relative position of the target is: ", rel_position)
    print("The Julian date of the observation is: ", julian_date)




if __name__ == '__main__':
    main()