# Problem 3069: Distribute Elements Into Two Arrays I

## Intuition
The problem seeks to distribute distinct elements of an array `nums` into two sub-arrays `arr1` and `arr2` using a series of operations. The core idea is to ensure that the larger element is always placed in the sub-array `arr1`. This strategy is based on the following observation: if the last element of `arr1` is greater than the last element of `arr2`, the next element should be added to `arr1`. Otherwise, it should be added to `arr2`. 

## Approach
1. **Initialization:** Create two empty arrays, `arr1` and `arr2`, to store the elements. 
2. **First Operations:** Append the first two elements of `nums` to `arr1` and `arr2` respectively. 
3. **Iterative Distribution:**  
   * **`for` loop:** Iterate from the third element of `nums`.
   * **Comparison:** For each element: 
      * If the last element of `arr1` is greater than the last element of `arr2`, append the current element to `arr1`.
      * Otherwise, append the current element to `arr2`.
4. **Concatenation:** Return the concatenation of `arr1` and `arr2`.

## Complexity Analysis
* **Time Complexity:** $O(n)$ - The algorithm iterates through the array `nums` for at most `n-2` operations. 
* **Space Complexity:** $O(1)$ - The algorithm uses only a few auxiliary arrays for temporary storage, resulting in constant space complexity.