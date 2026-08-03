# Problem 3689: Maximum Total Subarray Value I

## Intuition
The maximum total value can be achieved by choosing subarrays that maximize the range between their minimum and maximum values. The core idea is to calculate the sum of these ranges for all possible subarrays, then return the largest one.


## Approach
1. **Calculate Individual Range Values:** For each possible subarray (l..r), calculate the range using `max(nums[l..r]) - min(nums[l..r])`. 

2. **Group Subarrays into Optimal Sets:** This is crucial to find the best set of subarrays for maximum value. We need to define how to group subarrays based on their possible overlap, such as considering a subarray within a larger one if it provides additional range potential or more frequently selected subarrays.

3.  **Calculate Total Value:**  Iterate over all the chosen subarrays and calculate the total value for each set by summing up the individual range values of each subarray in the set. 
    
## Complexity Analysis
* **Time Complexity:** $O(N^2)$ - We iterate through the array `nums` to find the possible subarrays, which leads to a time complexity of `O(n * n)`. 
  * [Detailed explanation of why]

* **Space Complexity:** $O(1)$ 
    * The algorithm's space complexity is constant.