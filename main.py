import src as src

def main():
    planet_name = input("Enter the name of the planet where the observatory will be located: ")
    assert planet_name =='Mars', 'The planet name is not Mars, please enter the correct planet name'


    # Prompt the user to enter observatory latitude and Longitude
    location = input("Enter observatory latitude and longitude separated by commas (e.g., value1,value2): ")

    # Convert the input string to a tuple by splitting the string and then using tuple() to convert the list to a tuple
    latitude, longitude = tuple(location.split(','))

    print(latitude, longitude)  # This will print the tuple of values

    # initialize a new observatory object with the latitude and longitude
    observatory = src.Observatory(latitude, longitude)

    date_string = input("Enter the date in the format YYYY-MM-DD: ")

    planet = src.Planet()
    planet_data = src.load_planet(planet_name, date_string)
    # planet location on celestial sphere as seen from Earth
    planet.ra = planet_data['RA']
    planet.dec = planet_data['DEC']



if __name__ == '__main__':
    main()