# Problem 1340: Jump Game V

## Intuition
We can solve this problem by using dynamic programming. The idea is to use a `dp` array to store the maximum number of indices that can be visited starting at each index. We can go from one index to another by jumping either forward or backward, but we can only jump if the current element at index i  is greater than the element at index j, and the element at index i is greater than the element at every index between i and j. 

## Approach
1. **Initialization:** Create a `dp` array of size equal to the length of the input array `arr`. Initialize all elements in the `dp` array with 0. This will represent that no indices have been visited yet for each index.
2. **Dynamic Programming:** For each index `i`, use a recursive function `dfs(i)` to explore possible jumps. The recursion explores two possibilities at every step.  The base case is when `i` is equal to the last index of the array, meaning there are no more indices left to visit. 
3. **Exploring Jumps:** At each index `i`, we can jump to either the next position (`i + x`) or the previous position (`i - x`).  We do this by iterating over possible jumps and updating the `max_visited` variable accordingly. We keep track of the maximum number of indices that can be visited starting at each index using the `dp` array.
4. **Calculating Result:**  For every index `i`, we need to calculate the maximum number of indices that can be visited starting from that index by calling the `dfs(i)` function, which explores all possible jumps and update the `overall_max` variable accordingly.


## Complexity Analysis
* **Time Complexity:** $O(N)$ 
    * We iterate over each element in the input array once to explore all possible jumps at each index.   
* **Space Complexity:** $O(1)$
    * We use a constant amount of space for the `dp` array, regardless of the size of the input array.