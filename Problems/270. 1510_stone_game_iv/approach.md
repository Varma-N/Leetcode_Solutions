# Problem 1510: Stone Game IV

## Intuition
Alice and Bob play a game where each player can remove any number of non-zero square numbers of stones from a pile. The game ends when one player cannot make a legal move. This problem determines whether Alice will win the game. 

The core idea is to utilize dynamic programming to determine whether Alice can win the game. We can solve the problem using a table `dp` where `dp[i]` denotes whether Alice can win after removing `i` stones. 

## Approach
1. **Initialization:** We create a boolean array `dp` of size `n + 1` initialized to `False`. 
2. **Iteration:**
   -  Iterate from 1 to `n` (inclusive).
   - For each `i`, we start checking for `i` being a perfect square. We begin with `j = 1`.
   - Inside the `while` loop, we check if `j*j` is less than or equal to `i`.
     - If `j * j <= i`, we update `dp[i] = True` (Alice can win) and break the loop. 
     - If `j * j > i`, we increment `j` to check the next perfect square.
3. **Result:** Finally, return `dp[n]`, which indicates whether Alice wins.

## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the input `n`. We have a single loop that iterates for each possible number of stones.
* **Space Complexity:** $O(N)$ where N is the input `n`. The space complexity comes from the dynamic programming table `dp`, which uses `n + 1` entries to store the results.