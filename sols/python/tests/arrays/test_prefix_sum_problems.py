"""Prefix problems tests."""
from code_challenges.arrays.prefix_sum_problems import sum_absolute_differences


def test_sum_absolute_differences():
    """Test sum abs diff."""
    assert sum_absolute_differences([2, 3, 5]) == [4, 3, 5]
