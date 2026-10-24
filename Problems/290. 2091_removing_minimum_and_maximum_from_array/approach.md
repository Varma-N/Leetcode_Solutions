# Problem 2091: Removing Minimum and Maximum From Array

## Intuition
The solution leverages the fact that the minimum and maximum elements can be removed from an array by removing just the minimum and maximum elements. This is a problem of finding the minimum number of deletions.  The minimum deletions are achieved by finding the positions of the minimum and maximum values in the array. By doing so, the minimum number of deletions is determined.


## Approach
1. **Find the indices of the minimum and maximum elements:**  
   * Use `nums.index(min(nums))` to find the index of the minimum element. 
   * Use `nums.index(max(nums))` to find the index of the maximum element.
2. **Determine the deletion positions:** 
   *  Calculate the number of deletions required to remove the minimum and maximum elements using the index of the minimum and maximum elements. This is calculated using `min(j + 1, n - i, i + 1 + n - j)`

## Complexity Analysis
* **Time Complexity:** $O(1)$
    *  We are simply identifying the positions of the minimum and maximum elements using `index`. 
* **Space Complexity:** $O(1)$
    * The algorithm does not use any extra space.