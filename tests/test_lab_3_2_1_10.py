"""
Tests : 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater
Link  : https://edube.org/learn/pe-1/lab-the-continue-statement-the-ugly-vowel-eater-3
"""

from exercises.lab_3_2_1_10 import ExerciseLab


def test_sample_1():
    """Test sample 1 from exercise"""
    lab = ExerciseLab()

    # First sample
    lab.set_exercise_input("Gregory")
    actual = lab.run()

    assert "GRGRY" == actual


def test_sample_2():
    """Test sample 2 from exercise"""
    lab = ExerciseLab()

    # First sample
    lab.set_exercise_input("abstemious")
    actual = lab.run()

    assert "BSTMS" == actual


def test_sample_3():
    """Test sample 3 from exercise"""
    lab = ExerciseLab()

    # First sample
    lab.set_exercise_input("IOUEA")
    actual = lab.run()

    assert "" == actual
