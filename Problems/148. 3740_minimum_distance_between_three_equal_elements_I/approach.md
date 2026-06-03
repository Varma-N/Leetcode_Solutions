### Step-by-Step Approach

1.  **Group Indices by Value:** Iterate through the given array and create a mapping (like a hash map or dictionary) where each unique number is a key. The corresponding value for each key should be a list of all the indices where that number appears in the array. Because we process the array from left to right, these index lists will naturally be in strictly increasing order.

2.  **Initialize Tracking Variables:** Set up a variable to keep track of the minimum distance found so far. Initialize this with a very large value (e.g., infinity). Also, create a boolean flag to track whether you have successfully found at least one valid triplet during the process.

3.  **Filter Invalid Candidates:** Iterate through the grouped index lists in your map. If a number appears fewer than 3 times (i.e., the length of its index list is less than 3), it is impossible to form a triplet. Skip these numbers entirely.

4.  **Apply a Sliding Window of Size 3:** For each valid index list (length $\ge 3$), use a sliding window approach to evaluate adjacent triplets. By checking the element at index $z$ and the element at $z + 2$ within the list, you isolate three consecutive occurrences of the same number. 

5.  **Calculate and Update Minimum Distance:** For each triplet window, calculate the distance using the formula $2 \times (\text{index}[z+2] - \text{index}[z])$. Compare this current distance to your globally tracked minimum distance. If the current distance is smaller, update the minimum distance and set your boolean flag to true.

6.  **Final Evaluation:** After checking all possible triplets across all grouped values, check your boolean flag. If it is true, return the globally tracked minimum distance. If it is false (meaning no valid triplets existed in the entire array), return $-1$.

---

### Complexity Analysis

* **Time Complexity:** $O(N)$
    Where $N$ is the total number of elements in the array. We iterate through the array exactly once to populate the hash map, which takes $O(N)$ time. Then, we iterate through the index lists. Even though there is a nested loop, each index from the original array is processed exactly once during the window sliding phase. Therefore, the total time spent traversing the lists is strictly bounded by $O(N)$.

* **Space Complexity:** $O(N)$
    In the worst-case scenario (e.g., all elements are unique or all elements are the same), the hash map will store exactly $N$ indices distributed among its keys. This requires $O(N)$ auxiliary space.
