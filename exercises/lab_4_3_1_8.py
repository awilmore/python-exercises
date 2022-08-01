"""
Exercise : 4.3.1.8 LAB: Day of the year: writing and using your own functions
Link     : https://edube.org/learn/pe-1/lab-day-of-the-year-writing-and-using-your-own-functions-2
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 4.3.1.8 LAB: Day of the year: writing and using your own functions
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Check if leap year"""
        (year, month, day_of_month) = self.exercise_input

        # Validate input
        if year < 0 or month < 1 or month > 12 or day_of_month < 0:
            return None

        # Validate day_of_month is less than days for that month
        if day_of_month > self.days_in_month(year, month):
            return None

        # Prepare output
        day_of_year = 0

        # Count up to present month
        for i in range(1, month):
            day_of_year += self.days_in_month(year, i)

        # Add day of month
        day_of_year += day_of_month

        # Finished
        return day_of_year

    @staticmethod
    def days_in_month(year, month):
        """Determine number of days in month"""
        # Months with 31 days
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31

        # Months with 30 days
        if month in [4, 6, 9, 11]:
            return 30

        # Handle February on leap year
        if ExerciseLab.is_leap_year(year):
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
