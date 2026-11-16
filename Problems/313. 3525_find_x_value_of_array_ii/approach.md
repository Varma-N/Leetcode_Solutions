```markdown
# Problem 3525: Find X Value of Array II

## Intuition
The problem involves calculating the x-value of an array after applying a series of operations. The key is understanding how to leverage a modified prefix sum tree to efficiently store and retrieve information about the products of subarrays. This allows us to quickly determine the x-value after each modification.

## Approach
1. **Prefix Sum Tree (PS):** 
   * A prefix sum tree is used to efficiently store and retrieve information about the products of subarrays within the `nums` array.
   * The tree's structure allows us to quickly determine the product of a subarray for a given index, reducing the number of operations required. 
2. **Build the PS Tree:** 
   * The PS tree is built using the `build` function. 
   * This function divides the array into sub-arrays, calculates the product of each sub-array, and stores the results in the tree structure. 
3. **Update the PS Tree:**
   * The `update` function updates the product of a specific subarray in the tree. 
   * This function utilizes binary search to efficiently find the index in the array and update the tree. 
4. **Query the PS Tree:**
   * The `query` function uses binary search to determine the x-value for a given x-value in the array. 
   *  The function then retrieves the product corresponding to the x-value, returning the result.

## Complexity Analysis
* **Time Complexity:** $O(N \log N)$ 
    * The time complexity is dominated by the `build`, `update`, and `query` functions, where the time complexity of binary search is $O(logN)$.
* **Space Complexity:** $O(N)$ 
    * The space complexity is dominated by the size of the prefix sum tree, which can be $O(N)$ in the worst-case scenario.