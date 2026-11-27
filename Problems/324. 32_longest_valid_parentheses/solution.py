class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0 
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length) 
        
        return max_length