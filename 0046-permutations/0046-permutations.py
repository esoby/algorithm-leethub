class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = [(nums, [])]

        while stack:
            curr, tmp = stack.pop()

            if not curr:
                ans.append(tmp)

            for i in range(len(curr)):
                stack.append((curr[:i] + curr[i+1:], tmp + [curr[i]]))

        return ans
        
# from itertools import permutations
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return (permutations(nums, len(nums)))