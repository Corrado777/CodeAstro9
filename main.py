import src as src

def main():
    planet_name = input("Enter the name of the planet where the observatory will be located: ")
    assert planet_name =='Mars', 'The planet name is not Mars, please enter the correct planet name'

    # Grab the data and initialize a planet object given the planet name


    # Prompt the user to enter observatory latitude and Longitude
    location = input("Enter observatory latitude and longitude separated by commas (e.g., value1,value2): ")

    # Convert the input string to a tuple by splitting the string and then using tuple() to convert the list to a tuple
    latitude, longitude = tuple(location.split(','))

    print(latitude, longitude)  # This will print the tuple of values


if __name__ == '__main__':
    main()