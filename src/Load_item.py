#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:40:48 2024

@author: joshuaweston

Function to pull solar system planetary data for a given time.

Dependencies:
    

Input:
    Planet Name
    Datetime
    
Output:
    
    
"""

import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os

def load_planet(name,date):
    
    #generate dictionary of solar system planets and corresponding JPL Horizons keys
    planets = {
    'mercury': {'id': 199},
    'venus': {'id': 299},
    'earth': {'id': 10},
    'mars': {'id': 499},
    'jupiter': {'id': 599},
    'saturn': {'id': 699},
    'uranus': {'id': 799},
    'neptune': {'id': 899}  
                        }
    #Check input is valid
    
    if name.lower() not in planets:
        print("wrong!")
        return
    
    else:
        
        #Format date ('borrowed' wholesale from solarsysdaily)
        
        date_obs = date.split("-")
        yyyy,mm,dd = int(date_obs[0]),str(date_obs[1]),int(date_obs[2])
        if yyyy < 1 or yyyy > 9999:
            print("Invalid date: year must be between 1 and 9999")
            print("Returning \"None\" and stopping.")
            return None

        date_in = '{}-'.format(yyyy)+mm+'-{}'.format(dd)+' 00:01'
        date_next = '{}-'.format(yyyy)+mm+'-{}'.format(dd)+' 23:59'
        
        #JPL Request
        URL_pre = 'https://ssd.jpl.nasa.gov/api/horizons.api?format=text&'
        planet = 'COMMAND=\'{}\'&'.format(planets[name.lower()]['id'])
        ephem_setting = 'OBJ_DATA=\'YES\'&MAKE_EPHEM=\'YES\'&EPHEM_TYPE=\'OBSERVER\'&'
        obs = 'CENTER=\'50\'&'
        duration='START_TIME=\''+date_in+'\'&STOP_TIME=\''+date_next+'\'&STEP_SIZE=\'1%20d\'&'
        data = 'QUANTITIES=\'2,19,20\'&'
        ang = 'ANG_FORMAT=\'DEG\'&'
        csv_format = 'CSV_FORMAT=\'YES\''
        URL = str(URL_pre+planet+ephem_setting+obs+duration+data+ang+csv_format)
        r = requests.get(url = URL)
        data = r.content
        content = data.decode()
        
        # Extract relevant data
        lines = content.splitlines()
        data = None
        for i, line in enumerate(lines):
            if line == "$$SOE":
                data = lines[i + 1]
                break
    
        if data is None:
            print("No data found")
            return
    
        dataformatted = data.split(',')
    
        # Initialize variables
        obliquity = vol_mean_radius = sidereal_rot_period = None
    
        # Extract sidereal rotation period and volumetric mean radius from physical data section
        for line in lines:
            if "Sidereal rot. period" in line:
                sidereal_rot_period = float(line.split('=')[1].split()[0])
            if "Vol. mean radius (km)" in line:
                vol_mean_radius = float(line.split('=')[1].split()[0].split('+')[0])
            if "Obliquity to orbit" in line:
                obliquity = float(line.split('=')[1].split()[0].strip().replace("'", ""))
    
        # Construct data dictionary
        if name.lower() == 'earth':
            datadict = {
                "NAME": name.lower(),
                "DATE": date,
                "RA": float(dataformatted[3]),
                "DEC": float(dataformatted[4]),
                "HELRANGE": float(dataformatted[7]),
                "EARTHRANGE": float(dataformatted[5])
            }
        else:
            datadict = {
                "NAME": name.lower(),
                "DATE": date,
                "RA": float(dataformatted[3]),
                "DEC": float(dataformatted[4]),
                "HELRANGE": float(dataformatted[5]),
                "EARTHRANGE": float(dataformatted[7]),
                "SIDEREAL_ROT_PERIOD": sidereal_rot_period,
                "VOL_MEAN_RADIUS": vol_mean_radius,
                "OBLIQUITY TO ORBIT": obliquity
            }
    
        return datadict
    
    
def test_datadict():
    
    assert load_planet("Pluto","1996-09-13") == None
    
    assert load_planet("Earth","0000-01-01") == None
    
    test_dict = load_planet("Mercury","2000-01-01")
    
    assert test_dict['NAME'] == "mercury"
    
    assert isinstance(test_dict['OBLIQUITY TO ORBIT'],float)
    
    assert isinstance(test_dict['DATE'], str)

    test_dict_earth = load_planet("Earth","2024-07-18")
    
    assert test_dict_earth['EARTHRANGE'] == 0
    
    print("tests for load_item.py passed")
    
    pass

test_datadict()
    
