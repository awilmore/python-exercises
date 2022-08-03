"""
See lab file
"""

from exercises.lab_4_5_1_7 import ExerciseLab

###
# GLOBALS
###


def test_sample_1():
    """Assert break conditions"""
    assert ExerciseLab.fibonacci(1) == 1
    assert ExerciseLab.fibonacci(2) == 1


def test_sample_2():
    """Assert fib single digits"""
    assert ExerciseLab.fibonacci(3) == 2
    assert ExerciseLab.fibonacci(5) == 5
    assert ExerciseLab.fibonacci(7) == 13
    assert ExerciseLab.fibonacci(9) == 34


def test_sample_3():
    """Assert fib double digits"""
    assert ExerciseLab.fibonacci(11) == 89
    assert ExerciseLab.fibonacci(31) == 1346269


def test_sample_4():
    """Assert negative numbers returns None"""
    assert ExerciseLab.fibonacci(-1) is None
