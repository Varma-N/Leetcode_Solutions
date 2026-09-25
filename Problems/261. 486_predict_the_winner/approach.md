# Problem 486: Predict the Winner

## Intuition
The game's winner is decided by which player gets a larger score after removing the smallest and largest numbers at each turn. We can leverage dynamic programming to determine which player has the higher final score.  

## Approach
1. **Initialization:**
   *   `n = len(nums)`:  Gets the length of the input array `nums`.
   *   `dp = nums[:]`: Creates a copy of the input array `nums` and initializes it to be the same as `nums`.

2. **Dynamic Programming:**
    *   The core logic lies in the `for diff in range(1, n)` loop. We iterate through possible differences (`diff`) in the array, representing the range of elements to be taken from.
    *   For each `diff`, we use nested loops to consider all possible choices (`left` and `right`) starting from the `left`th index and ending at the `right`th index.
    *   Within this loop:
        *   `dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])`:  This is the heart of the dynamic programming approach. It calculates the maximum possible score for the current player. 

3. **Final Check:**
   *   `return dp[0] >= 0`: After all iterations, we check if Player 1's score (`dp[0]`) is greater than or equal to 0. 


## Complexity Analysis
* **Time Complexity:** $O(N^2)$
    * The algorithm visits each element in the input array multiple times.
* **Space Complexity:** $O(N)$
    *  We store the `dp` array, which is the same size as the input array.