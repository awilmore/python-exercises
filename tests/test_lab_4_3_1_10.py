"""
See lab file
"""

from exercises.lab_4_3_1_10 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_to_mpg():
    """Verify conversion 1"""
    assert LAB.litres_100km_to_miles_gallon(3.9) == 60.311431623931625
    assert LAB.litres_100km_to_miles_gallon(7.5) == 31.361944444444443
    assert LAB.litres_100km_to_miles_gallon(10.0) == 23.521458333333328


def test_sample_to_100km():
    """Verify conversion 1"""
    assert LAB.miles_gallon_to_litres_100km(60.3) == 3.900739358761747
    assert LAB.miles_gallon_to_litres_100km(31.4) == 7.490910297239915
    assert LAB.miles_gallon_to_litres_100km(23.5) == 10.009131205673759
