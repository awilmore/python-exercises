"""
See lab file
"""

from exercises.lab_4_3_1_6 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample 1 from exercise"""
    LAB.set_exercise_input(1900)
    assert not LAB.run()


def test_sample_2():
    """Test sample 2 from exercise"""
    LAB.set_exercise_input(2000)
    assert LAB.run()


def test_sample_3():
    """Test sample 3 from exercise"""
    LAB.set_exercise_input(2016)
    assert LAB.run()


def test_sample_4():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input(1987)
    assert not LAB.run()


def test_sample_5():
    """Test sample 5 from exercise"""
    LAB.set_exercise_input(2022)
    assert not LAB.run()


def test_sample_6():
    """Test sample 6 from exercise"""
    LAB.set_exercise_input(2024)
    assert LAB.run()
