# Problem 1855: Maximum Distance Between a Pair of Values

## Approach

### Step-by-Step Breakdown

1.  **Initialize Pointers and Tracker:**
    * Start with two pointers, `i` for `nums1` and `j` for `nums2`, both initialized to 0. 
    * Initialize `max_dist` to 0 to store the largest distance found between a valid pair $(i, j)$.
2.  **Iterate with Two Pointers:**
    * Use a `while` loop to traverse both arrays simultaneously while both pointers are within their respective bounds.
3.  **Validate Condition and Calculate Distance:**
    * Check if the condition `nums1[i] <= nums2[j]` is met.
    * If valid:
        * Calculate the current distance `j - i`. 
        * Update `max_dist` if this distance is greater than the current maximum.
        * Increment `j` to search for potentially larger distances further in `nums2`.
    * If invalid (i.e., `nums1[i] > nums2[j]`):
        * Increment `i` to move to a smaller value in `nums1`, as the current `nums1[i]` is too large to satisfy the non-increasing condition with the current `nums2[j]`.
4.  **Return Result:**
    * Once the loop completes, return the `max_dist`.



## Complexity Analysis

* **Time Complexity:** $O(N + M)$
    * Where $N$ is the length of `nums1` and $M$ is the length of `nums2`. Each pointer (`i` and `j`) only moves forward and traverses its respective array at most once, resulting in a linear time complexity.
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of extra space (three integer variables) regardless of the size of the input arrays.
