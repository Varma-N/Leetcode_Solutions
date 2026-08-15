# Problem 1833: Maximum Ice Cream Bars

## Intuition
The problem involves finding the maximum number of ice cream bars a boy can purchase using a given budget.  We can solve this problem by using a counting sort approach. The essence of the algorithm is to use a count array to track the frequency of each ice cream bar price, then, greedily buy the cheapest ice cream bars first, stopping when the remaining budget is insufficient to purchase any more bars.

## Approach
1. **Calculate the Maximum Ice Cream Bar Price:** First, find the maximum price of an ice cream bar using `max(costs)`. This is crucial for calculating the maximum number of bars we can buy. 

2. **Initialize the Frequency Array:** Create an array `freq` of size `max_cost + 1`, initialized with zeros. This array will store the frequency of each price level of the ice cream bars. 

3. **Populate the Frequency Array:** Iterate through the input `costs` array and increment the count in `freq` for each `cost`. This counts the number of times each bar price appears in the `costs` array.

4. **Greedy Purchase:** Initialize `total_bars` to 0. We'll use a loop to iteratively buy the cheapest ice cream bars.  
    - **Check for Affordability:**  If the remaining budget (`coins`) is less than the price of the current ice cream bar (`price`), we cannot buy any more bars at the current price. Stop the loop.  
    - **Calculate Number of Bars to Buy:** Calculate `bars_we_can_buy` based on the frequency of the current price (`freq[price]`) and the amount of coins remaining (`coins`).  This determines how many bars we can buy at this particular price.  
    - **Update Totals:** Add `bars_we_can_buy` to `total_bars` to represent the number of bars we have bought.  Subtract the cost of these bars from the `coins` to reflect the budget.

5. **Return the Result:** After the loop completes, return the `total_bars` which represents the maximum number of ice cream bars the boy can buy. 

## Complexity Analysis
* **Time Complexity:** $O(n + max(costs))$ 
    * `freq` array is filled in $O(n)$ time.
    * Looping over `costs` is $O(n)$ time. 
    * The rest of the algorithm is $O(1)$. 
* **Space Complexity:** $O(max(costs))$ 
    * The `freq` array uses space proportional to the maximum price.