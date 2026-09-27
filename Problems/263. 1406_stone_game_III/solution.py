class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3
        
        for i in range(n - 1, -1, -1):
            ans = float('-inf')
            score = 0
            for j in range(1, 4):
                if i + j <= n:
                    score += stoneValue[i + j - 1]
                    ans = max(ans, score - dp[(i + j) % 3])
            dp[i % 3] = ans
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"