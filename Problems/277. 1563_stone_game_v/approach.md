# Problem 1563: Stone Game V

## Intuition
Alice and Bob play a game where Alice strategically divides a row of stones and Bob calculates the value of each row. Alice scores points based on the sum of the stones remaining in the row after Bob's calculated value. This game involves a series of rounds with a focus on maximizing the scoring potential for Alice based on the calculated values.

## Approach
1. **Calculate Prefixes:** The code begins by creating a prefix array `prefix`. This array stores the sum of all the stones from the beginning to each index `i`.
2. **Create DP Table:** The code then creates a 2D array `dp`, a 2D array `max_l`, and a 2D array `max_r`. 
3. **Initialize `max_l` and `max_r`:** The `max_l` and `max_r` arrays will store the maximum score that Alice can achieve based on the left and right rows at each index, initialized to the value of the current stone at the index itself.
4. **Iterate and Compute Scores:** The code then uses a nested loop to iterate through all possible ranges of `i` and `j`, calculating the maximum score Alice can achieve at each step using dynamic programming.
5. **Calculate `dp` Array:** The `dp` array is used to store the calculated scores for each possible score range at each step.  The `dp` array can be used to calculate the maximum score for any given range of `i` and `j` after each iteration.
6. **Return `dp[0][n-1]`:** After the loop is finished, the `dp` array contains the maximum score Alice can achieve at the end of the game.


## Complexity Analysis
* **Time Complexity:** $O(N^2)$
    * The nested loop iterates through all possible ranges of `i` and `j` within the `dp` array.
* **Space Complexity:** $O(N^2)$
    * The `dp` array stores the maximum score for each possible game state.