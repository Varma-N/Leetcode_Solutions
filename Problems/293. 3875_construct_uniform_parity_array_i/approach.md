# Problem 3875: Construct Uniform Parity Array I

## Intuition
The core idea is to exploit the fact that we only need to choose one element from the input array to make the resulting array's parity consistent.  By iterating through the input array, we can efficiently create a new array where all elements are either even or odd, based on the selection criteria. 


## Approach
1. **Initialization:** 
   -  Create an empty array `nums2` of the same length as `nums1`.

2. **Iteration:**
   -  Loop through each index `i` in `nums1`.
   - For each index `i`, choose a value from the following options:
     - **Option 1:**  `nums2[i] = nums1[i]`. 
     - **Option 2:**  `nums2[i] = nums1[i] - nums1[j]`,  for an index `j` != `i`, i.e., calculate the difference with another element `j` not equal to `i`.
   
3. **Parity Check:**
   -  For each `i`, check if the element in `nums2[i]` is even or odd. If it's even, continue to the next step.  If it's odd, then we can conclude that the array can be constructed.
   -  **Note:** We do not need to check for odd parity for each element in the array.  
   -  This allows us to efficiently construct the desired array by ensuring parity is consistent throughout the array.


## Complexity Analysis
* **Time Complexity:** $O(n)$ 
    * We iterate through the `nums1` array once to make the selections. The time complexity is dependent on the number of elements in `nums1`.
* **Space Complexity:** $O(n)$
    * We need to store the `nums2` array, and the size of `nums2` is proportional to the size of `nums1`.