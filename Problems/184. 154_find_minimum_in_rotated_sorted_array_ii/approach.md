# Problem 154: Find Minimum in Rotated Sorted Array II

## Intuition
The key to solving this problem lies in utilizing the fact that the array is sorted and rotated.  We can leverage binary search to efficiently find the minimum element within the rotated array. By focusing on comparing elements at the mid-point with the right end, we can determine if the middle element is larger than the right endpoint. If it is, we know the left boundary must be shifted, indicating a potential smaller value in that range. 

## Approach
1. **Initialization:** We start with two pointers, `left` and `right`, initially set to the beginning and end of the array (`0` and `len(nums) - 1`).
2. **Binary Search Loop:**  We enter a while loop where we continue as long as `left` is less than `right`. 
   * Inside the loop, calculate the middle index `mid = (left + right) // 2`.
   * **Comparison:** We compare the element at the middle (`nums[mid]`) with the element at the right end (`nums[right]`): 
      * If  `nums[mid]` is greater than `nums[right]`, it means the minimum must be in the left half, so we move `left` to `mid + 1`.  
      * If `nums[mid]` is smaller than `nums[right]`, the minimum must be in the right half, so we move `right` to `mid`. 
      * If `nums[mid]` equals `nums[right]`, this means we found an equal element at that index. We need to adjust our search to find the actual minimum in the array. So, we decrease `right` by 1.

3. **Result:** After the loop ends, we have narrowed down the search space and `left` points to the index of the minimum element.


## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The binary search algorithm visits roughly half of the array in each iteration, leading to a time complexity of $O(log(n))$ (the number of iterations is proportional to the logarithm of n). 
* **Space Complexity:** $O(1)$
    * We are using only a constant amount of extra space.
