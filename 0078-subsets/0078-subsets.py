from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        q = deque([[n] for n in nums])

        while q:
            arr = q.popleft()
            ans.append(arr)

            for i in nums:
                if arr[-1] < i:
                    tmp = arr.copy()
                    tmp.append(i)
                    q.append(tmp)
                
        return ans