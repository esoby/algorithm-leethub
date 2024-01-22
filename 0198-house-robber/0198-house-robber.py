class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        max_val = nums[0]

        for i in range(2, len(nums)):
            max_tmp = -1
            for j in range(i - 1):
                max_tmp = max(max_tmp, nums[j])
            nums[i] += max_tmp
            max_val = max(max_val, nums[i])
        
        return max_val