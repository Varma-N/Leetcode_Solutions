class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Add the boundary fences
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        # Compute all possible vertical distances
        v_diffs = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_diffs.add(v[j] - v[i])

        max_side = 0

        # Compute horizontal distances and check if they exist in vertical distances
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                d = h[j] - h[i]
                if d in v_diffs:
                    max_side = max(max_side, d)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD
