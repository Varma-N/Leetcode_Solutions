# Problem 3116: Kth Smallest Amount With Single Denomination Combination

## Intuition
To solve this problem, we must understand the concept of Least Common Multiple (LCM) of a set of numbers. We must then employ a binary search algorithm to efficiently find the kth smallest amount that can be made from the given coins.

## Approach
1. **Calculate LCMs:**
   - We initialize an empty list `lcm_list` to store the LCMs of all possible subsets of the coins. 
   - Using bit manipulation, we build a set of all possible subsets of the coins using a binary representation of the numbers in `lcm_list`. 
   - The `curr_lcm` variable, initialized to 1, calculates the LCM for each subset.  
2. **Binary Search:**
   - We set `low` and `high` to 1 and the minimum coin value (`min(coins)`) multiplied by `k` respectively. 
   - We perform a binary search on the `lcm_list` to determine the kth smallest amount using `res = sum(sign * (mid // val) for val, sign in lcm_list)`. 

3. **Return:**
    - Finally, the function returns the `ans` value representing the kth smallest amount.


## Complexity Analysis
* **Time Complexity:** $O(N*log(2^N))$ where N is the number of coins. 
    * This is due to the binary search algorithm for determining the kth smallest amount. 
* **Space Complexity:** $O(N)$
    * We are storing all the numbers in the `lcm_list`, which requires $O(N)$ space.