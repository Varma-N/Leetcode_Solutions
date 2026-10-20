class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left, right = 0, 0
        ones_count = 0
        best = None
        while right < len(s):
            if s[right] == '1':
                ones_count += 1
            while ones_count == k:
                current_sub = s[left:right+1]
                if (best is None or 
                    len(current_sub) < len(best) or 
                    (len(current_sub) == len(best) and current_sub < best)):
                    best = current_sub
                if s[left] == '1':
                    ones_count -= 1
                left += 1
            right += 1
        return best if best is not None else ""