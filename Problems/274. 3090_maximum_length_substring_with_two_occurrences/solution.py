class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        d = {}
        max_length = 0
        while right < n:
            d[s[right]] = d.get(s[right], 0) + 1
            while d[s[right]] > 2:
                d[s[left]] = d[s[left]] - 1
                left += 1
            current_valid_substring_length = right - left + 1
            max_length = max(max_length, current_valid_substring_length)
            right += 1
        return max_length