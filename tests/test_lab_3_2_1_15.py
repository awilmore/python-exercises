"""
See lab file
"""

from exercises.lab_3_2_1_15 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample 1 from exercise"""
    LAB.set_exercise_input(15)
    assert LAB.run() == 17


def test_sample_2():
    """Test sample 2 from exercise"""
    LAB.set_exercise_input(16)
    assert LAB.run() == 4


def test_sample_3():
    """Test sample 3 from exercise"""
    LAB.set_exercise_input(1023)
    assert LAB.run() == 62


def test_sample_4():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input(0)
    assert LAB.run() == 0


def test_sample_5():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input(-1)
    assert LAB.run() == 0
