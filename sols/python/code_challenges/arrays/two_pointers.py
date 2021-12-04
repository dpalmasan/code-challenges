"""Array problems that might be solved by two pointers technique."""
from typing import List


class MaxSubarrayDivideAndConquer:
    """Implement Max subarray using a Divide and Conquer approach."""

    def cross_sum(self, nums: List[int], low: int, high: int, mid: int) -> int:
        """Compute the maximum sum of a subarray passing through the middle.

        Input: nums = [5,4,-1,7,8]
        Output: 23

        Input: nums = [1]
        Output: 1

        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.

        This is ``O(n)`` in complexity.

        :param nums: List of numbers
        :type nums: List[int]
        :param low: Lower limit of the subarray
        :type low: int
        :param high: Upper limit of the subarray
        :type high: int
        :param mid: Mid section
        :type mid: int
        :return: Maximum sum crossing the mid section
        :rtype: int
        """
        left_max_sum = nums[mid]
        left_sum = nums[mid]
        i = mid - 1
        while i >= low:
            left_sum += nums[i]
            if left_sum > left_max_sum:
                left_max_sum = left_sum
            i -= 1

        i = mid + 2
        right_max_sum = nums[mid + 1]
        right_sum = nums[mid + 1]
        i = mid + 2
        while i <= high:
            right_sum += nums[i]
            if right_sum >= right_max_sum:
                right_max_sum = right_sum
            i += 1
        return left_max_sum + right_max_sum

    def divide_and_conquer(self, nums: List[int], low: int, high: int) -> int:
        """Recursive step for the divide and conquer implementation.

        :param nums: List of numbers
        :type nums: List[int]
        :param low: Lower limit of the subarray
        :type low: int
        :param high: Upper limit
        :type high: int
        :return: Maximum sum of a subarray between low and upper limit.
        :rtype: int
        """
        if low >= high:
            return nums[low]

        mid = (low + high) // 2
        left_sum = self.divide_and_conquer(nums, low, mid)
        right_sum = self.divide_and_conquer(nums, mid + 1, high)
        cross_sum = self.cross_sum(nums, low, high, mid)
        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: List[int]) -> int:
        """Implement a divide and conquer solution.

        This algorithm is ``O(nlog(n))`` and it is based on the idea of
        solving separate subproblems and combining to get to the
        final solution.

        :param nums: Input array
        :type nums: List[int]
        :return: Max subarray sum
        :rtype: int
        """
        return self.divide_and_conquer(nums, 0, len(nums) - 1)


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
