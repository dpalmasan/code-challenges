"""Test cases for spiral matrix traversal."""
import pytest
from sols.arrays.spiral import spiral


def test_base_cases():
    """Test base cases."""
    assert spiral(1) == [[1]]
    assert spiral(2) == [[1, 2], [4, 3]]


def test_odd_case():
    """Test odd case."""
    assert spiral(3) == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]


def test_even_case():
    """Test big even case."""
    assert spiral(8) == [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [28, 29, 30, 31, 32, 33, 34, 9],
        [27, 48, 49, 50, 51, 52, 35, 10],
        [26, 47, 60, 61, 62, 53, 36, 11],
        [25, 46, 59, 64, 63, 54, 37, 12],
        [24, 45, 58, 57, 56, 55, 38, 13],
        [23, 44, 43, 42, 41, 40, 39, 14],
        [22, 21, 20, 19, 18, 17, 16, 15],
    ]


def test_negative_case():
    """Test for invalid inputs."""
    with pytest.raises(ValueError):
        spiral(0)
