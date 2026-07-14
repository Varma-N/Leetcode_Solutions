# Problem 2657: Find the Prefix Common Array of Two Arrays

## Intuition
The solution leverages the properties of permutations and counting to efficiently determine the prefix common array of two given arrays. By iterating through both input arrays, we identify occurrences of elements within each array using a set to track seen elements.  We maintain a count for the number of common elements encountered at each index and append it to our result array. 

## Approach
1. **Initialization:**
    * `res`: An empty list to store the prefix common counts, initialized with length equal to the input arrays' sizes (to facilitate appending the results).
    * `seen`: An empty set is used to efficiently track the unique elements encountered in both arrays. This will be crucial for determining the count of shared elements. 

2. **Iterative Counting:**
    * Iterate through both input arrays (`A` and `B`) using an index `i`.
        *  **Check for Common Elements:** For each element (`A[i]`, `B[i]`), if it is found within the `seen` set, increment the common count (`common_count`). Otherwise, add the element to the `seen` set. 
    * **Append Count to Result:** After each iteration of the inner loop, append `common_count` to the `res` array. 

3. **Return Prefix Common Array:** After processing both input arrays, return the `res` list, containing the prefix common counts for each index (`i`).  


## Complexity Analysis
* **Time Complexity:** $O(n)$ - The algorithm iterates through the length of the input arrays once to determine the count of common elements in both arrays. 
* **Space Complexity:** $O(n)$ - We store at most `n` unique elements within the `seen` set, where `n` represents the length of the arrays.