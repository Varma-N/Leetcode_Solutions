class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # dist = 0
        n = len(words)
        res = n
        found = False
        for i in range(n):
            if words[i] == target:
                found = True
                d_dist = abs(i - startIndex)
                c_dist = n - d_dist
                res = min(res, d_dist, c_dist)
        return res if found else -1
