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
