class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        res = list(s1)
        for i in range(2):
            if s1[i] == s2[i]:
                continue
            res[i], res[i + 2] = s1[i + 2], s1[i]
            if ''.join(res) == s2:
                return True
        return ''.join(res) == s2
        
