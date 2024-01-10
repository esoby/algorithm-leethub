class Solution:
    def combine(self, n: int, k: int):
        ans = []
        stack = [(i, [i]) for i in range(1, n+1)]

        while stack:
            num, tmp = stack.pop()
            if len(tmp) == k:
                ans.append(tmp)
            elif num < n:
                for i in range(num+1, n+1):
                    stack.append((i, tmp + [i]))

        return ans

# from itertools import combinations
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         return list(combinations(range(1, n+1), k))