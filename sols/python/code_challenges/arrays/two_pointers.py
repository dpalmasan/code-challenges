"""Array problems that might be solved by two pointers technique."""
from typing import List


def rotate_naive(nums: List[int], k: int) -> None:
    """Do not return anything, modify nums in-place instead."""
    kp = k % len(nums)
    if kp == 0:
        return
    backup = list(nums)
    for i in range(len(nums)):
        new_idx = (i + kp) % len(nums)
        nums[new_idx] = backup[i]


def rotate_mem_opt(nums: List[int], k: int) -> None:
    """Do not return anything, modify nums in-place instead."""
    kp = k % len(nums)
    if kp == 0:
        return
    i1 = 0
    backup_val = nums[0]
    loop_start = 0
    for _ in nums:
        i2 = (i1 + kp) % len(nums)
        tmp = nums[i2]
        nums[i2] = backup_val
        backup_val = tmp
        i1 = i2
        if i1 == loop_start:
            loop_start += 1
            i1 = loop_start % len(nums)
            backup_val = nums[i1]


def max_sub_array_sum(nums: List[int]) -> int:
    """Get the maximum subarray sum of a given array.

    :param nums: List of numbers
    :type nums: List[int]
    :return: Max subarray sum
    :rtype: int
    """
    max_sum = nums[0]
    total_sum = max_sum
    j = 1
    while j < len(nums):
        if total_sum < 0:
            total_sum = 0
        else:
            total_sum += nums[j]
            if total_sum > max_sum:
                max_sum = total_sum
            j += 1

    return max_sum
