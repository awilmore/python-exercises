"""
Exercise : 3.2.1.15 LAB: Collatz's hypothesis
Link     : https://edube.org/learn/pe-1/lab-collatz-s-hypothesis-3
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 3.2.1.15 LAB: Collatz's hypothesis
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Apply Collatz formula"""
        c_value = int(self.exercise_input)
        steps = 0

        while c_value > 1:
            if c_value % 2 == 0:
                c_value //= 2
            else:
                c_value = 3 * c_value + 1

            steps += 1

        return steps
