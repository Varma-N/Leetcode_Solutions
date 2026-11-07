import collections
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        B = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        
        counts = collections.Counter()
        for r1, c1 in A:
            for r2, c2 in B:
                counts[(r2 - r1, c2 - c1)] += 1
               
        return max(counts.values()) if counts else 0
