class Solution:
    def backtrack(self, i, nums, curr_sum, max_sum, cache) -> int:
        if i >= len(nums):
            return max_sum

        curr_sum += nums[i]
        max_sum = max(max_sum, curr_sum)
        j = i + 2
        while j < len(nums):
            max_sum = max(
                self.backtrack(j, nums, curr_sum, max_sum, cache), max_sum
            )
            j += 1

        curr_sum -= nums[i]
        max_sum = max(
            max_sum, self.backtrack(i + 1, nums, curr_sum, max_sum, {})
        )

        return max_sum

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        max_sum = 0
        max_sum = max(max_sum, self.backtrack(0, nums, 0, max_sum, {}))
        return max_sum


# print(Solution().rob([2,7,9,3,1])) # 12
# print(Solution().rob([2, 1, 1, 2])) # 4
# print(Solution().rob([4,1,2,7,5,3,1])) # 14
# print(Solution().rob([6,3,10,8,2,10,3,5,10,5,3])) # 39
