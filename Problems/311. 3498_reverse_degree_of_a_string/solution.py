class Solution:
    def reverseDegree(self, s: str) -> int:
        res, idx = 0, 1
        for ch in s:
            res += (123 - ord(ch)) * idx
            idx += 1
        return res