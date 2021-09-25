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
    prefix = [0]*(n + 1)
    for i in range(1, len(nums) + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
        
    result = [0]*n
    for i in range(n):
        result[i] = (
            prefix[n] - prefix[i + 1] - nums[i]*(n - i - 1)
            - prefix[i] + nums[i]*i
        )
    return result
