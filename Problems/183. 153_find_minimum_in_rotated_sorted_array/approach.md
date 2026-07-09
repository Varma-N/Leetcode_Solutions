# Problem 153: Find Minimum in Rotated Sorted Array

## Intuition
Finding the minimum element in a rotated sorted array requires identifying the smallest element amongst those elements after rotation.  The intuition lies in understanding that with each rotation, the minimum element's position might change due to its original position being in an unsorted portion of the array. The solution leverages this by utilizing binary search on the left side of the array and exploiting the sorted property of the array to locate the smallest element.

## Approach
1. **Initialization:** 
   *  `last_index = len(nums)-1` : Initialize a variable `last_index` to track the index of the last element in the array. 
2. **Boundary Check:** 
   * If `nums[0] > nums[last_index]` then check if we are at the end of the rotation.  Otherwise, proceed with binary search on the left side:
3. **Binary Search (if applicable):** 
    * The array is sorted and rotated in place, so it can be assumed to be a single-element solution for all cases.


## Complexity Analysis
* **Time Complexity:** $O(log n)$
    * The algorithm iterates through the array with each rotation of `n` positions.  
* **Space Complexity:** $O(1)$ 
    *  The algorithm uses a constant amount of extra space, independent of the input size.