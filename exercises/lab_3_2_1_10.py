"""
Exercise : 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater
Link     : https://edube.org/learn/pe-1/lab-the-continue-statement-the-ugly-vowel-eater-3
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Split word into letters, skip vowels"""
        output = []

        # Process input (expect string)
        for char in str(self.exercise_input).upper():
            if char in ["A", "E", "I", "O", "U"]:
                continue

            output.append(char)

        # Return result
        return "".join(output)
