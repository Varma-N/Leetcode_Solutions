# Problem 1406: Stone Game III

## Intuition
The key is understanding that both players play optimally, meaning each player wants to maximize their score relative to the other player. This implies we can evaluate the game by calculating the maximum score difference (current player's score minus the opponent's score) from any given state. Since the choice at any step only depends on the outcomes of the next 1, 2, or 3 possible moves, we can solve this using Dynamic Programming by working backward from the end of the array. To optimize space, we only need to keep track of the last 3 states.

## Approach
1. **Initialization:** 
    * Get the length of the `stoneValue` array, denoted as `n`.
    * Create a `dp` array of size 3, initialized to 0. This will store the maximum score difference for the current player at a given step. 

2. **Iterate Backwards:**
    * Loop `i` from `n - 1` down to 0. Working backward ensures that when we are at step `i`, the answers for `i + 1`, `i + 2`, and `i + 3` are already computed.
    
3. **Calculate Best Move for Current State:**
    * For each index `i`, initialize `ans` to negative infinity and a running `score` to 0. 
    * Iterate `j` from 1 to 3 (representing taking 1, 2, or 3 stones). 
    * If `i + j <= n`, add the value of the taken stone (`stoneValue[i + j - 1]`) to `score`.
    * Calculate the relative score difference if this move is chosen: `score - dp[(i + j) % 3]`. The `dp` term represents the best score difference the *opponent* can achieve from the remaining stones.
    * Update `ans` to be the maximum of its current value and this new relative score difference.

4. **Update DP Array:**
    * Store the best possible score difference `ans` into `dp[i % 3]`. Using the modulo operator (`% 3`) automatically overwrites older states we no longer need, keeping our space usage strictly constant.

5. **Determine the Winner:**
    * After the loop finishes, `dp[0]` holds the maximum score difference for Alice at the very start of the game.
    * **Case 1:** If `dp[0] > 0`, Alice's score is strictly greater than Bob's, so return "Alice".
    * **Case 2:** If `dp[0] < 0`, Bob's score is strictly greater than Alice's, so return "Bob".
    * **Case 3:** If `dp[0] == 0`, their scores are equal, so return "Tie".

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The algorithm iterates through the `stoneValue` array of length $N$ exactly once. In each iteration, it performs a constant maximum of 3 inner loop steps.
* **Space Complexity:** $O(1)$
    * The algorithm only uses a `dp` array of size 3 and a few integer variables (`n`, `ans`, `score`, `i`, `j`), which require constant auxiliary space regardless of the input size.