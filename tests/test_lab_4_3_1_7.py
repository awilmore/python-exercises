"""
See lab file
"""

from exercises.lab_4_3_1_7 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample 1 from exercise"""
    LAB.set_exercise_input((1900, 2))
    assert LAB.run() == 28


def test_sample_2():
    """Test sample 2 from exercise"""
    LAB.set_exercise_input((2000, 2))
    assert LAB.run() == 29


def test_sample_3():
    """Test sample 3 from exercise"""
    LAB.set_exercise_input((2016, 1))
    assert LAB.run() == 31


def test_sample_4():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input((1987, 11))
    assert LAB.run() == 30


def test_sample_5():
    """Test sample 5 from exercise"""
    LAB.set_exercise_input((2001, 2))
    assert LAB.run() == 28


def test_sample_6():
    """Check invalid input 1"""
    LAB.set_exercise_input((-100, 2))
    assert LAB.run() is None


def test_sample_7():
    """Check invalid input 2"""
    LAB.set_exercise_input((2000, -2))
    assert LAB.run() is None


def test_sample_8():
    """Check invalid input 3"""
    LAB.set_exercise_input((2000, 13))
    assert LAB.run() is None
