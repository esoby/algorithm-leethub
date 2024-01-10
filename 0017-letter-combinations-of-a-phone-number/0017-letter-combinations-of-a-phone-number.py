import string

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        alpha = string.ascii_lowercase
        ans = []
        my_dict = {}

        for s in digits:
            idx = (int(s) - 2) * 3
            if s == '7':
                val = alpha[idx : idx+4]
            elif s == '8':
                val = alpha[idx+1 : idx+4]
            elif s == '9':
                val = alpha[idx+1 : idx+5]
            else:
                val = alpha[idx : idx+3]
            my_dict[s] = list(val)

        stack = ['']

        while stack:
            print(stack)
            word = stack.pop()
            if len(word) == len(digits):
                ans.append(word)
            else:
                for c in my_dict[digits[len(word)]]:
                    stack.append(word + c)

        return ans