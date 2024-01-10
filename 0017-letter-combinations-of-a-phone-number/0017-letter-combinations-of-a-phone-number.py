import string

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        alpha = string.ascii_lowercase
        ans = []
        my_dict = {}

        dial = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        for s in digits:
            my_dict[s] = dial[s]

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

# from itertools import product  
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if digits == "":
#             return []
#         dial = {
#         '2' : 'abc',
#         '3' : 'def',
#         '4' : 'ghi',
#         '5' : 'jkl',
#         '6' : 'mno',
#         '7' : 'pqrs',
#         '8' : 'tuv',
#         '9' : 'wxyz'
#         }

#         dials = [dial[x] for x in digits]
#         com = list(product(*dials))
#         answer = [''.join(x) for x in com]
#         return answer