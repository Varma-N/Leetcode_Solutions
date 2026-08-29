class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue
                
                max_sum = -1
                ways = 0
                
                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n and dp[ni][nj][1] > 0:
                        if dp[ni][nj][0] > max_sum:
                            max_sum = dp[ni][nj][0]
                            ways = dp[ni][nj][1]
                        elif dp[ni][nj][0] == max_sum:
                            ways = (ways + dp[ni][nj][1]) % MOD
                
                if ways > 0:
                    val = 0 if board[i][j] == 'E' else int(board[i][j])
                    dp[i][j] = [max_sum + val, ways]

        return dp[0][0] if dp[0][0][1] > 0 else [0, 0]