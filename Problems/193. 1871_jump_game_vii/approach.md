# Problem 1871: Jump Game VII

## Intuition
At first glance, the problem appears difficult due to the need to traverse a binary string. However, we can simplify it by recognizing that the only possible movement is in the direction of '0's. By utilizing a recursive approach to check for reachable indices, we can determine if we can reach the last index ('s.length - 1') within a specific jump limit. 

## Approach
1. **Initialization:** 
    *  Set `reachable` array of size equal to length of string `s` and initialize all elements to `False`, marking each index as unreachable initially.
    * Set `reachable[0]` to `True`, representing the initial starting point at index 0.
2. **Active Jumps:** 
    * Initialize `active_jumps` to zero, representing the number of jumps we can currently take. 
3. **Iteration and Movement:** 
    * Loop through each character of string `s` from index 1 onwards (using a loop from `i = 1` to  'n'):
      * For each index `i`:
        * Check if `i >= minJump` and `reachable[i - minJump]`. If true, then `active_jumps` is incremented. 
        *  Check if `i > maxJump` and `reachable[i - maxJump - 1]` (this ensures movement towards the end of the string). This helps keep track of how many jumps are allowed.
        * If both conditions hold true, the current index `i` can be made reachable. Set `reachable[i]` to `True`.  

4. **Final Check:** 
    *  After iterating through each character, return `reachable[-1]`, which represents if we can reach the last index of the string.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through every character in the string once to determine if a jump is possible. 
* **Space Complexity:** $O(1)$
    * The algorithm uses only a few auxiliary variables like `reachable` array and `active_jumps`, which are constant in size.
