from heapq import heapify, nsmallest

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        sums = [(sum(row), i) for i, row in enumerate(mat)] 
        heapify(sums)

        return [idx for (num, idx) in nsmallest(k, sums)]