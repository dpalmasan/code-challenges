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
    n = len(nums)
    total_sum = sum(nums)  
    result = [0]*n
    cum_sum = 0
    cum_sum_next = 0
    for i in range(n):
        cum_sum_next += nums[i]
        result[i] = total_sum - cum_sum_next - nums[i]*(n - i - 1) + nums[i]*i - cum_sum
        cum_sum += nums[i]
    return result
