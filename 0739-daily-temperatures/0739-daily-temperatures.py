class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for cur_day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                prev_day, _ = stack.pop()
                ans[prev_day] = cur_day - prev_day
            stack.append((cur_day, temp))

        return ans
