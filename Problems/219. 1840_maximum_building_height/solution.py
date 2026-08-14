class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        
        m = len(restrictions)
        
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])
            
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
            
        ans = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            ans = max(ans, (h1 + h2 + id2 - id1) // 2)
            
        ans = max(ans, restrictions[-1][1] + n - restrictions[-1][0])
        
        return ans