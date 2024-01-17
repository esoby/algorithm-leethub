# 버블 정렬
class Solution:
    def sortColors(self, nums):
        iters = len(nums) - 1

        for iter in range(iters):
            wall = iters - iter
            print(wall)
            for cur in range(wall):
                if nums[cur] > nums[cur + 1]:
                    nums[cur], nums[cur + 1] = nums[cur + 1], nums[cur]

        return nums
