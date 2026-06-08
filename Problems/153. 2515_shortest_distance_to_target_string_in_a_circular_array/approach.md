# Problem 2515: Shortest Distance to Target String in a Circular Array

## Approach

### Step-by-Step Breakdown

1.  **Initialize Variables:**
    * Store the length of the `words` array as `n`.
    * Initialize a result variable `res` with `n` (the maximum possible distance in a circular array) and a boolean `found` flag to `False` to track if the target exists.
2.  **Iterate Through the Array:**
    * Loop through every index `i` of the `words` array.
3.  **Check for Target Match:**
    * If `words[i]` matches the `target`:
        * Set `found` to `True`.
        * Calculate the direct distance as `d_dist = abs(i - startIndex)`.
        * Calculate the circular distance as `c_dist = n - d_dist`.
        * Update `res` to be the minimum of its current value, the direct distance, and the circular distance.
4.  **Return Result:**
    * After the loop, check the `found` flag. If `True`, return `res`; otherwise, return `-1` to indicate the target was not present.

## Complexity Analysis

* **Time Complexity:** $O(N)$
    * $N$ is the number of words in the array. The algorithm performs a single pass over the array, performing $O(1)$ calculations at each index.
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of extra space (a few integer and boolean variables), regardless of the input size.
