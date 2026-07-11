# Problem 1306: Jump Game III

## Intuition
The key to solving this problem is understanding that we can reach any index with a value of 0 if it's reachable from the start. This requires us to explore all possible jump paths, considering valid jumps within the array boundaries and ensuring we don't go outside the array.


## Approach
1. **Initialization:**  Define `n` as the length of the input array `arr`, and initialize a set `visited` to track visited indices during DFS.

2. **Depth-First Search (DFS):** Implement a recursive DFS function called `dfs(i)` that explores the graph starting at index `i`.
   * **Base Case:** If `i` is out of bounds (`i < 0 or i >= n`) or if it's already visited, return `False` as we cannot explore this path. 
   * **Target Check:** If `arr[i]` equals 0 (target reached), return `True`.
   * **Exploring Jumps:**  Mark the current index `i` as visited and recursively call `dfs(i + arr[i])` to explore jumps to the right and `dfs(i - arr[i])` for jumps to the left. 

3. **Root Call:** Start DFS from the initial index `start` using `dfs(start)`.


## Complexity Analysis
* **Time Complexity:**  The time complexity is  $O(N)$ because we explore all potential paths, where N is the length of the array.
    * The DFS function explores each possible jump path by visiting at most every node (the maximum number of nodes is equal to the number of steps). 
* **Space Complexity:**  The space complexity is $O(N)$ due to storing visited indices in the `visited` set. We need to store all visited indices to avoid revisiting them.