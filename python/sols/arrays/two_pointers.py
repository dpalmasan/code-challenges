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
