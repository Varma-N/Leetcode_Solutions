# 3010. Divide an Array Into Subarrays With Minimum Cost I — Approach

## Step-by-Step Approach

1. The first element of the array must always be included in the cost, so store `nums[0]`.
2. Extract the remaining elements of the array starting from index `1`.
3. Sort the remaining elements in ascending order.
4. Select the two smallest elements from the sorted remaining array.
5. Add the first element and the two smallest elements to get the minimum possible cost.
6. Return the computed sum.

## Time Complexity
- **O(n log n)**  
  - Sorting the remaining `n-1` elements dominates the runtime.

## Space Complexity
- **O(n)**  
  - Additional space is used to store the sliced array of remaining elements.
