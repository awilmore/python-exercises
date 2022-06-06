"""
See lab file
"""

from exercises.lab_4_3_1_8 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample input"""
    LAB.set_exercise_input((1900, 1, 1))
    assert LAB.run() == 1


def test_sample_2():
    """Test sample input"""
    LAB.set_exercise_input((1900, 2, 1))
    assert LAB.run() == 32


def test_sample_3():
    """Test sample input"""
    LAB.set_exercise_input((1900, 12, 31))
    assert LAB.run() == 365


def test_sample_4():
    """Test sample input"""
    LAB.set_exercise_input((2000, 12, 31))
    assert LAB.run() == 366


def test_sample_5():
    """Test sample input"""
    LAB.set_exercise_input((2001, 4, 1))
    assert LAB.run() == 91


def test_sample_6():
    """Edge cases"""
    LAB.set_exercise_input((2000, 1, 32))
    assert LAB.run() is None


def test_sample_7():
    """Edge cases"""
    LAB.set_exercise_input((2000, 2, 32))
    assert LAB.run() is None


def test_sample_8():
    """Edge cases"""
    LAB.set_exercise_input((-2000, 1, 1))
    assert LAB.run() is None
