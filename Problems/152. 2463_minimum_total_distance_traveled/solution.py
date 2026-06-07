class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factory_positions = []
        for pos, limit in factory:
            factory_positions.extend([pos] * limit)
            
        n, m = len(robot), len(factory_positions)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][m] = float('inf')
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                skip = dp[i][j + 1]
                take = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]
                
                dp[i][j] = min(skip, take)
                
        return dp[0][0]
