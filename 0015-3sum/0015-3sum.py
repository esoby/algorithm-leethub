class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        for left in range(len(nums)-2):

            if left > 0 and nums[left] == nums[left - 1]:
                continue
            move = left + 1
            right = len(nums)-1
            
            while move < right:
                if left == move:
                    break
                sum = nums[left] + nums[move] + nums[right]
                    
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    move += 1
                else: 

                    ans.append( [nums[left], nums[move], nums[right]] )
                    right -= 1
                    
                    while move < right and nums[move] == nums[move - 1]:
                        move += 1

                    while move < right and nums[right] == nums[right + 1]:
                        right -= 1
                

        return ans