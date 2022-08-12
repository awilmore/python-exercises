"""
Exercise : 4.5.1.7 LAB: Creating functions - Fibonacci numbers (recursive)
Link     : https://edube.org/learn/pe-1/creating-functions-fibonacci-numbers-3
"""


# pylint: disable=R0801,R0903
class ExerciseLab:
    """
    Exercise : 4.5.1.7 LAB: Creating functions - Fibonacci numbers
    """

    @staticmethod
    def fibonacci(num):
        """Break conditions"""
        if num < 1:
            return None

        if num < 3:
            return 1

        # Recursive call
        return ExerciseLab.fibonacci(num - 1) + ExerciseLab.fibonacci(num - 2)
