class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {'(': ')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in parentheses_dict:
                stack.append(i)
            elif stack and i == parentheses_dict[stack[-1]]:
                stack.pop()
            else: return False
        return not stack