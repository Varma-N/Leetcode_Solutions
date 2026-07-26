class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse = True)
        if n <= 2:
            return sum(cost)
        total_cost = 0
        for i in range(0, n, 3):
            total_cost += sum(cost[i:i+2])    
        return total_cost