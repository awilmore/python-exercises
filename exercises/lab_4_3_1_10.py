"""
Exercise : 4.3.1.10 LAB: Converting fuel consumption
Link     : https://edube.org/learn/pe-1/lab-converting-fuel-consumption-3
"""

# Globals
MILE = 1.609344  # metres
GALLON = 3.785411784  # litres


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 4.3.1.10 LAB: Converting fuel consumption
    """

    @staticmethod
    def litres_100km_to_miles_gallon(fuel_rate):
        """Convert per km to per mile, then calculate per gallon"""
        litres_per_mile = (fuel_rate / 100) * MILE
        gallon_per_mile = litres_per_mile / GALLON

        # Return reciprocal
        return 1 / gallon_per_mile

    @staticmethod
    def miles_gallon_to_litres_100km(fuel_rate):
        """Convert gallon to litre, then calculate per 100km"""
        miles_per_litre = fuel_rate / GALLON
        km_per_litre = miles_per_litre * MILE

        # Invert and multiply by 100
        return (1 / km_per_litre) * 100
