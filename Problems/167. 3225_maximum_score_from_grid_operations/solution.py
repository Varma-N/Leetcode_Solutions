class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        P = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                P[c][r + 1] = P[c][r] + grid[r][c]

        INF = -10**18
        dp = [[INF] * (n + 1) for _ in range(n + 1)]
        for j in range(n + 1):
                dp[0][j] = 0

        for c in range(n):
            new_dp = [[INF] * (n + 1) for _ in range(n + 1)]
            for j in range(n + 1):  
                pref = [INF] * (n + 1)
                cur = INF
                for i in range(n + 1):
                    if dp[i][j] > cur:
                        cur = dp[i][j]
                    pref[i] = cur
                suff_ge = [INF] * (n + 2)
                cur = INF
                for i in range(n, -1, -1):
                    val = dp[i][j] + P[c][i]
                    if val > cur:
                        cur = val
                    suff_ge[i] = cur

                p1 = pref[j - 1] if j > 0 else INF
                p2 = suff_ge[j] - P[c][j] if suff_ge[j] != INF else INF
                cv = p1 if p1 > p2 else p2

                for k in range(j):
                    new_dp[j][k] = cv

                for k in range(j, n + 1):
                    t1 = (pref[k] + P[c][k]) if pref[k] != INF else INF
                    t2 = suff_ge[k + 1]
                    val = t1 if t1 > t2 else t2
                    if val != INF:
                        new_dp[j][k] = val - P[c][j]

            dp = new_dp
        return max(dp[j][0] for j in range(n + 1))