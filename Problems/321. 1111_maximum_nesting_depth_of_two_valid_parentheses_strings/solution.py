class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        level = 0
        for i in seq:
            if i == "(":
                res.append(level % 2)
                level += 1
            elif i == ")":
                level -= 1
                res.append(level % 2)    
        return res