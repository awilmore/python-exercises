"""
See lab file
"""

from exercises.lab_3_2_1_14 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample 1 from exercise"""
    LAB.set_exercise_input(6)
    assert LAB.run() == 3


def test_sample_2():
    """Test sample 2 from exercise"""
    LAB.set_exercise_input(20)
    assert LAB.run() == 5


def test_sample_3():
    """Test sample 3 from exercise"""
    LAB.set_exercise_input(1000)
    assert LAB.run() == 44


def test_sample_4():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input(2)
    assert LAB.run() == 1


def test_sample_5():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input(0)
    assert LAB.run() == 0


def test_sample_6():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input(-10)
    assert LAB.run() == 0
