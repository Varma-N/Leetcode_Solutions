class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        stack = []
        current_string = ""
        for ch in s:
            if ch == '(':
                stack.append(current_string)
                current_string = ""
            
            elif ch == ')':
                temp = stack.pop()
                current_string = temp + current_string[::-1] 

            else:
                current_string += ch
        return current_string