def test_calc_pos():
    """
    Unit test for the function calc_pos_target_rel_planet()
    """
    import os, sys 
    sys.path.insert(0, '../src/')
    from planet import Planet 
    from Load_item import load_planet
    from astropy.coordinates import SkyCoord
    from calc_pos import calc_pos_target_rel_planet
    import pytest

    # step 1: choose a target 
    planet_obj = Planet()
    target_label = 'M31'

    #step 2: Load planet data and assign it to planet object as an attribute 
    planet_data = load_planet('Mars', '01-01-2000')
    planet_obj.ra = planet_data['RA']
    planet_obj.dec = planet_data['DEC']

    #step: Call the calc_pos_target_rel_planet() function 
    result = calc_pos_target_rel_planet(planet_obj, target_label)

    #step: declare expected results 
    expected_ra = 10.6847083
    expected_dec = 41.26875

    assert expected_ra == pytest.approx(result.ra.value, abs=1e-3)
    assert expected_dec == pytest.approx(result.dec.value, abs=1e-3)
    pass 