class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        
        # Step 2: Initialize the frequency array
        freq = [0] * (max_cost + 1)
        
        # Populate the frequency array
        for cost in costs:
            freq[cost] += 1
            
        total_bars = 0
        
        # Step 3: Greedily buy the cheapest ice creams first
        for price in range(1, max_cost + 1):
            if freq[price] > 0:
                # If we don't even have enough coins for one bar at this price, stop
                if coins < price:
                    break
                
                # Calculate how many bars we can buy at this specific price
                bars_we_can_buy = min(freq[price], coins // price)
                
                # Update our totals and remaining coins
                total_bars += bars_we_can_buy
                coins -= price * bars_we_can_buy
                
        return total_bars