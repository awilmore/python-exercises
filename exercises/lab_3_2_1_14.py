"""
Exercise : 3.2.1.14 LAB: Essentials of the while loop
Link     : https://edube.org/learn/pe-1/lab-essentials-of-the-while-loop-3
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 3.2.1.14 LAB: Essentials of the while loop
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Calculate height of box pyramid"""
        block_limit = int(self.exercise_input)
        block_count = height = 0

        # Add blocks while less than limit
        while block_count < block_limit:
            height += 1
            block_count += height

        # Revert unnecessary increment
        if block_count != block_limit and block_limit > 0:
            height -= 1

        return height
