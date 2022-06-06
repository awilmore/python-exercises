"""
Exercise : 4.3.1.7 LAB: How many days: writing and using your own functions
Link     : https://edube.org/learn/pe-1/lab-how-many-days-writing-and-using-your-own-functions-2
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 4.3.1.7 LAB: How many days: writing and using your own functions
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Check if leap year"""
        (year, month) = self.exercise_input

        # Months with 31 days
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31

        # Months with 30 days
        if month in [4, 6, 9, 11]:
            return 30

        # Handle February on leap year
        if self.is_leap_year(year):
            return 29

        # Regular year
        return 28

    @staticmethod
    def is_leap_year(year):
        """Determine whether year is leap year"""
        if year % 4 == 0:
            return year % 100 != 0 or year % 400 == 0

        # Not a leap year
        return False
