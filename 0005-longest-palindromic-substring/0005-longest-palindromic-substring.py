class Solution:
    def expand(s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1: j]

    def longestPalindrome(self, s: str) -> str:
        answer = s[0]

        for i in range(len(s)):
            cand = Solution.expand(s, i, i)
            if len(cand) > len(answer):
                answer = cand

        for i in range(len(s) - 1):
            cand = Solution.expand(s, i, i+1)
            if len(cand) > len(answer):
                answer = cand

        return answer