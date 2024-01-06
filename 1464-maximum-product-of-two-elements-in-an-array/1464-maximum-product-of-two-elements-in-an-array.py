from heapq import heapify, nlargest

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapify(nums)
        return reduce(lambda x, y: (x - 1) * (y - 1), nlargest(2, nums))