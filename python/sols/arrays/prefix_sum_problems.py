"""Pre-fix problems."""
from typing import List


def sum_absolute_differences(nums: List[int]) -> List[int]:
    """Return sum of absolute differences of each element.

    For example, if we have the input [2, 3, 5], the result would be:

    - result[0] = |2 - 3| + |2 - 5| = 4
    - result[1] = |3 - 2| + |3 - 5| = 3
    - result[2] = |5 - 2| + |5 - 3| = 5

    :param nums: Input array
    :type nums: List[int]
    :return: Result with sum of absolute differences
    :rtype: List[int]
    """
    total_sum = sum(nums)
    result = [0] * len(nums)
    cum_sum = 0
    cum_sum_next = 0
    for i, el in enumerate(nums):
        cum_sum_next += el
        result[i] = (
            total_sum
            - cum_sum_next
            + el * ((i << 1) - len(nums) + 1)
            - cum_sum
        )
        cum_sum += el
    return result
