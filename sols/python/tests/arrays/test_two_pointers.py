"""Test cases for two_pointers."""
from code_challenges.arrays.two_pointers import (
    rotate_naive,
    rotate_mem_opt,
    MaxSubarrayDivideAndConquer,
    max_sub_array_sum,
)


def test_sample_cases():
    """Sample cases."""
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_naive(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    k = 2
    rotate_naive(nums, k)
    assert nums == [3, 99, -1, -100]

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_mem_opt(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    k = 2
    rotate_mem_opt(nums, k)
    assert nums == [3, 99, -1, -100]


def test_360_rotation():
    """Test 360 degree rotation ``k == nums.length``."""
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = len(nums)
    rotate_naive(nums, k)
    assert nums == [1, 2, 3, 4, 5, 6, 7]

    k = len(nums)
    rotate_mem_opt(nums, k)
    assert nums == [1, 2, 3, 4, 5, 6, 7]


def test_360_and_k_rotation():
    """Test 360 degree rotation plus ``k``."""
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = len(nums) + 3
    rotate_naive(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = len(nums) + 3
    rotate_mem_opt(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_max_subarray_sum():
    """Simple test cases for max subarray sum."""
    nums = [5, 4, -1, 7, 8]
    assert (
        MaxSubarrayDivideAndConquer().max_sub_array(nums)
        == 23
        == max_sub_array_sum(nums)
    )

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert (
        MaxSubarrayDivideAndConquer().max_sub_array(nums)
        == 6
        == max_sub_array_sum(nums)
    )

    nums = [1]
    assert (
        MaxSubarrayDivideAndConquer().max_sub_array(nums)
        == 1
        == max_sub_array_sum(nums)
    )
