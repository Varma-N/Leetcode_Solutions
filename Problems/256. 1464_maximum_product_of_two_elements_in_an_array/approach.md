# Problem 1464: Maximum Product of Two Elements in an Array

## Intuition
Given an array of integers `nums`, the goal is to find the maximum product of two elements in the array after subtracting 1 from each. The key insight is that the maximum product is achieved by selecting the two largest elements in the array. The `nums.sort()` operation allows us to quickly identify the largest elements. 

## Approach
1. **Sort the Array:** Sort the `nums` array using `nums.sort()`. This step is crucial to allow us to efficiently identify the two largest elements.
2. **Find the Largest Elements:** After sorting, the largest element will be at the end of the array (`nums[-1]`) and the second-largest element will be at the second-to-last index (`nums[-2]`).
3. **Calculate the Product:** Calculate the product of the largest element (`nums[-1]`) and the second-largest element (`nums[-2]`), and subtract 1 from each. 

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
```



## Complexity Analysis
* **Time Complexity:** $O(N \log N)$ 
    * Sorting the array in linear time, with an average of $O(N \log N)$ using `nums.sort()`.
* **Space Complexity:** $O(1)$
    *  The space complexity is constant as we only use a fixed amount of memory to store the input array.