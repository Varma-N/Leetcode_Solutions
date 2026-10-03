# Problem 1140: Stone Game II

## Intuition
The problem involves a sequence of turns where players can take a number of stones from a pile. The key is understanding the optimal strategy for Alice. This can be understood through the dynamic programming approach of solving the subproblems.

## Approach
1. **Initialization:**
   - `n`: Stores the number of piles.
   - `suffix_sum`: A list to store the sum of stones from the end of each pile to the start of each pile. 

2. **Dynamic Programming:**
   - We iterate through the `suffix_sum` list from right to left. For each pile, we add the current pile's stone count to the sum.
   - `@cache` decorator ensures that the `dfs` function only computes the results that haven't been computed before. 

3. **Recursive DFS:**
   - `dfs` function utilizes a recursive approach to simulate the game. 
   - It checks the maximum sum of stones after taking a certain number of stones, based on the remaining piles.
   - `best` variable tracks the maximum sum of stones.
   - `@cache` ensures that the result of each recursive call is cached, thus avoiding redundant calculations.

4. **Return Value:**
   - The function returns the calculated maximum stone count.



## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The time complexity of the `dfs` function is $O(N)$, where N is the number of piles. This is because the function has to visit each pile once. 
* **Space Complexity:** $O(N)$
    * The space complexity is $O(N)$ due to storing the `suffix_sum` list and the `dfs` function result.