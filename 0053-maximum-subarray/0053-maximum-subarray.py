class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_val = nums[0]

        for i in range(1, len(nums)):
            # i에서 새로 시작하기 vs 그동안의 부분 배열 합에 더하기
            nums[i] = max(nums[i], nums[i-1] + nums[i])
            max_val = max(max_val, nums[i])

        return max_val