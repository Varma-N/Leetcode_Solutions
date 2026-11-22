class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        current_count = 0
        for char in s:
            if char == '(': 
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            elif char ==')':
                current_count -= 1
        return max_count