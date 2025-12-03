class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(char)
            last = s.rfind(char)
            if first != -1 and last != -1 and first < last:
                result += len(set(s[first + 1 : last]))
        return result
