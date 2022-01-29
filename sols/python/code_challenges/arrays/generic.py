from typing import List
import heapq


def maximum_product_heap(nums: List[int]) -> int:
    """Compute the maximum triple product of an array.

    Copying is n, heapify is n, and extracting elements is ``O(n)``, but since we
    are always extracting the same amount of elements no matter the value of
    ``n`` in this case we have ``O(1)``. Thus, this approach is ``O(n)``.
    :param nums: [description]
    :type nums: List[int]
    :return: [description]
    :rtype: int
    """
    nums2 = list(nums)
    heapq._heapify_max(nums2)
    heapq.heapify(nums)
    min_mult = heapq.heappop(nums) * heapq.heappop(nums)
    max_val = heapq._heappop_max(nums2)
    return max(
        min_mult * max_val,
        max_val * heapq._heappop_max(nums2) * heapq._heappop_max(nums2),
    )


def maximum_product_sort(nums: List[int]) -> int:
    """Compute the maximum triple product of an array.

    The runtime of this algorithm is ``O(n logn)`` as it uses sorting.

    :param nums: [description]
    :type nums: List[int]
    :return: [description]
    :rtype: int
    """
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
