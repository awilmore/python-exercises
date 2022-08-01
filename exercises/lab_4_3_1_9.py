"""
Exercise : 4.3.1.9 LAB: Prime numbers - how to find them
Link     : https://edube.org/learn/pe-1/lab-prime-numbers-how-to-find-them-2
"""


# pylint: disable=R0801
class ExerciseLab:
    """
    Exercise : 4.3.1.9 LAB: Prime numbers - how to find them
    """

    def __init__(self):
        self.exercise_input = None

    def set_exercise_input(self, exercise_input):
        """Input to be used for exercise"""
        self.exercise_input = exercise_input

    def run(self):
        """Determine whether number is prime"""
        number = self.exercise_input

        # Negative number
        if number < 0:
            return False

        # First 3 primes
        if 0 < number < 4:
            return True

        # Determine prime
        upper_range = int(number ** 0.5) + 1
        for i in range(2, upper_range):
            if number % i == 0:
                return False

        # Not prime
        return True


#    def is_prime(self, number):
#        """Determine whether number is prime"""
#
#        # Check cache
#        if number in self.prime_list:
#            return True
#
#        # Calculate prime


