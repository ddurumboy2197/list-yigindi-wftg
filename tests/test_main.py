# test_list_sum.py
import pytest

def test_list_sum():
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([-1, 1, -2, 2, -3, 3]) == 0
    assert sum_list([]) == 0
    assert sum_list([10]) == 10
    assert sum_list([-10]) == -10

def sum_list(numbers):
    return sum(numbers)
