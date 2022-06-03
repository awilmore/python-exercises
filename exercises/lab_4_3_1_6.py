"""
Exercise : 4.3.1.6 LAB: A leap year: writing your own functions
Link     : https://edube.org/learn/pe-1/lab-a-leap-year-writing-your-own-functions-2
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 4.3.1.6 LAB: A leap year: writing your own functions
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Check if leap year"""
        year = self.exercise_input

        # Possible leap year
        if year % 4 == 0:
            return year % 100 != 0 or year % 400 == 0

        # Not a leap year
        return False
