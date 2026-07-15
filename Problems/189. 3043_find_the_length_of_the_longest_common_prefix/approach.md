# Problem 3043: Find the Length of the Longest Common Prefix

## Intuition
The solution leverages the properties of common prefixes and uses a set to store all possible prefixes of integers from `arr1`.  By iterating through `arr2`, we find the length of the longest common prefix for each pair. 


## Approach
1. **Prefix Generation:**  Convert each integer in `arr1` to a string using `str(num)`. Then, use nested loops to iterate through possible prefix lengths (`i`). 
    * For each prefix length `i`, extract all prefixes of the integers from `arr1`. We store these prefixes in a set called `prefixes`.
2. **Prefix Matching:**  For each integer in `arr2`:
    * Convert it into a string for easier processing.  
    * Iterate through possible prefix lengths (`i`). 
        * If the current prefix of `s` exists in the `prefixes` set, then update `max_length`. Otherwise, break the loop for that number. 
3. **Return:** The length of the longest common prefix is the final `max_length`.


## Complexity Analysis

* **Time Complexity:**  $O(N \cdot M)$, where N and M are the lengths of arr1 and arr2 respectively. We perform a nested loop over all prefixes for each element in arr2, resulting in linear complexity. 
    * The set `prefixes` allows us to efficiently check for common prefixes within O(1) time per prefix. 
* **Space Complexity:**  $O(N)$, storing the prefixes and the length of longest common prefix in a list.