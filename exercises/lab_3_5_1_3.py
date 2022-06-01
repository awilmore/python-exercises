"""
Exercise : 3.5.1.3 LAB: Sorting simple lists - the bubble sort algorithm
Link     : https://edube.org/learn/pe-1/sorting-simple-lists-the-bubble-sort-algorithm-11
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 3.5.1.3 LAB: Sorting simple lists - the bubble sort algorithm
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Implement bubble sort algorithm"""
        input_list = self.exercise_input
        sorted_list = input_list[:]
        swapped = True

        while swapped:
            swapped = False

            for i in range(len(sorted_list) - 1):
                if sorted_list[i] > sorted_list[i + 1]:
                    swapped = True
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]

        return sorted_list
