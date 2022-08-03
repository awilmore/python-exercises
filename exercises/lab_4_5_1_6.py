"""
Exercise : 4.5.1.6 LAB: Creating functions - factorials (recursive)
Link     : https://edube.org/learn/pe-1/creating-functions-factorials-3
"""


# pylint: disable=R0801,R0903
class ExerciseLab:
    """
    Exercise : 4.5.1.6 LAB: Creating functions - factorials
    """

    @staticmethod
    def factorial(num):
        """Break conditions"""
        if num < 0:
            return None

        if num < 2:
            return 1

        # Recursive call
        return num * ExerciseLab.factorial(num - 1)
