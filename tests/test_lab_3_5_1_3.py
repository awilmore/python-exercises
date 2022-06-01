"""
See lab file
"""

from exercises.lab_3_5_1_3 import ExerciseLab

###
# GLOBALS
###

LAB = ExerciseLab()


def test_sample_1():
    """Test sample 1 from exercise"""
    LAB.set_exercise_input([1])
    assert LAB.run() == [1]


def test_sample_2():
    """Test sample 2 from exercise"""
    LAB.set_exercise_input([1, 2, 3])
    assert LAB.run() == [1, 2, 3]


def test_sample_3():
    """Test sample 3 from exercise"""
    LAB.set_exercise_input([3, 2, 1])
    assert LAB.run() == [1, 2, 3]


def test_sample_4():
    """Test sample 4 from exercise"""
    LAB.set_exercise_input([1, 1, 1])
    assert LAB.run() == [1, 1, 1]


def test_sample_5():
    """Test sample 5 from exercise"""
    LAB.set_exercise_input([7, 3, 1, 8, 9, 0, 6, 4, 2, 5])
    assert LAB.run() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sample_6():
    """Test sample 6 from exercise"""
    LAB.set_exercise_input([3, 1, 3, 2, 3, 4, 3])
    assert LAB.run() == [1, 2, 3, 3, 3, 3, 4]


def test_sample_7():
    """Test sample 6 from exercise"""
    LAB.set_exercise_input([-1, -100, 100, 44])
    assert LAB.run() == [-100, -1, 44, 100]


def test_sample_8():
    """Test sample 8 from exercise"""
    LAB.set_exercise_input([-100])
    assert LAB.run() == [-100]


def test_sample_9():
    """Test sample 9 from exercise"""
    LAB.set_exercise_input([])
    assert LAB.run() == []
