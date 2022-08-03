"""
See lab file
"""

from exercises.lab_4_5_1_6 import ExerciseLab

###
# GLOBALS
###


def test_sample_1():
    """Assert 0! and 1! is 1"""
    assert ExerciseLab.factorial(0) == 1
    assert ExerciseLab.factorial(1) == 1


def test_sample_2():
    """Assert 2! is 2"""
    assert ExerciseLab.factorial(2) == 2


def test_sample_3():
    """Assert 3! is 6"""
    assert ExerciseLab.factorial(3) == 6


def test_sample_4():
    """Check range of factorials"""
    assert ExerciseLab.factorial(4) == 24
    assert ExerciseLab.factorial(5) == 120
    assert ExerciseLab.factorial(10) == 3628800
    assert ExerciseLab.factorial(16) == 20922789888000


def test_sample_5():
    """Assert negative numbers returns None"""
    assert ExerciseLab.factorial(-1) is None
