class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i not in dic:
                stack.append(i)
            # 닫는 괄호면 stack.pop()과 같으면 통과
            elif not stack or stack.pop() != dic[i]:
                return False
            
        return len(stack) == 0