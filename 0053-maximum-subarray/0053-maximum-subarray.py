class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = [0] * len(nums)
        memo[0] = nums[0]
        max_val = nums[0]

        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i-1] + nums[i])
            max_val = max(max_val, memo[i])

        return max_val