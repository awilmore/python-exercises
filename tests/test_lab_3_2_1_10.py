"""
See lab file
"""

from exercises.lab_3_2_1_10 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample 1 from exercise"""
    LAB.set_exercise_input("Gregory")
    assert LAB.run() == "GRGRY"


def test_sample_2():
    """Test sample 2 from exercise"""
    LAB.set_exercise_input("abstemious")
    assert LAB.run() == "BSTMS"


def test_sample_3():
    """Test sample 3 from exercise"""
    LAB.set_exercise_input("IOUEA")
    assert LAB.run() == ""
