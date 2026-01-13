from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int
    ) -> int:
        
        children = defaultdict(list)
        for u, v in hierarchy:
            children[u].append(v)
        
        NEG_INF = -10**9
        
        @lru_cache(maxsize=None)
        def dfs(node: int, boss_bought: bool):
            """
            Returns a tuple dp where:
            dp[cost] = max profit in subtree rooted at node
            using exactly 'cost' budget.
            """
            dp = [NEG_INF] * (budget + 1)
            
            # Determine price and profit
            price = present[node - 1] // 2 if boss_bought else present[node - 1]
            profit = future[node - 1] - price
            
            # Base DP for no children
            dp_no_buy = [0] + [NEG_INF] * budget
            
            # Merge children assuming node is NOT bought
            for child in children[node]:
                child_dp = dfs(child, False)
                new_dp = [NEG_INF] * (budget + 1)
                for c1 in range(budget + 1):
                    if dp_no_buy[c1] == NEG_INF:
                        continue
                    for c2 in range(budget - c1 + 1):
                        if child_dp[c2] == NEG_INF:
                            continue
                        new_dp[c1 + c2] = max(
                            new_dp[c1 + c2],
                            dp_no_buy[c1] + child_dp[c2]
                        )
                dp_no_buy = new_dp
            
            # Scenario: node IS bought
            dp_buy = [NEG_INF] * (budget + 1)
            if price <= budget:
                dp_buy[price] = profit
                for child in children[node]:
                    child_dp = dfs(child, True)
                    new_dp = [NEG_INF] * (budget + 1)
                    for c1 in range(budget + 1):
                        if dp_buy[c1] == NEG_INF:
                            continue
                        for c2 in range(budget - c1 + 1):
                            if child_dp[c2] == NEG_INF:
                                continue
                            new_dp[c1 + c2] = max(
                                new_dp[c1 + c2],
                                dp_buy[c1] + child_dp[c2]
                            )
                    dp_buy = new_dp
            
            # Combine both scenarios
            for i in range(budget + 1):
                dp[i] = max(dp_no_buy[i], dp_buy[i])
            
            return tuple(dp)
        
        final_dp = dfs(1, False)  # CEO has no boss
        return max(max(final_dp), 0)
