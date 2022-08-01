"""
See lab file
"""

from exercises.lab_4_3_1_9 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Assert 1 is prime"""
    LAB.set_exercise_input(1)
    assert LAB.run()


def test_sample_2():
    """Assert 2 is prime"""
    LAB.set_exercise_input(2)
    assert LAB.run()


def test_sample_3():
    """Assert 4 is not prime"""
    LAB.set_exercise_input(4)
    assert not LAB.run()


def test_sample_4():
    """Assert 15 is not prime"""
    LAB.set_exercise_input(15)
    assert not LAB.run()


def test_sample_5():
    """Assert 17 is prime"""
    LAB.set_exercise_input(17)
    assert LAB.run()


def test_sample_6():
    """Assert 36 is not prime"""
    LAB.set_exercise_input(36)
    assert not LAB.run()


def test_sample_7():
    """Assert 37 is prime"""
    LAB.set_exercise_input(37)
    assert LAB.run()


def test_sample_8():
    """Assert 1300 is not prime"""
    LAB.set_exercise_input(1300)
    assert not LAB.run()


def test_sample_9():
    """Assert 1301 is prime"""
    LAB.set_exercise_input(1301)
    assert LAB.run()


def test_sample_10():
    """Assert 7918 is not prime"""
    LAB.set_exercise_input(7918)
    assert not LAB.run()


def test_sample_11():
    """Assert 7919 is prime"""
    LAB.set_exercise_input(7919)
    assert LAB.run()


def test_sample_12():
    """Assert 999982 is not prime"""
    LAB.set_exercise_input(999982)
    assert not LAB.run()


def test_sample_13():
    """Assert 999983 is prime"""
    LAB.set_exercise_input(999983)
    assert LAB.run()
