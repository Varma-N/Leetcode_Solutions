# Problem 2161: Partition Array According to Given Pivot

## Intuition
The core idea of the algorithm is based on partitioning the array into three sections: elements smaller than the pivot, equal to the pivot, and elements greater than the pivot.  This approach allows for a straightforward rearrangement of the elements within each section to achieve the desired order according to the pivot. This can be implemented using a simple loop. 


## Approach
1. **Initialization:**  Create three empty lists: `less`, `equal`, and `greater`. These will store elements less than, equal to, and greater than the pivot respectively.

2. **Iteration:** Iterate through each element (`num`) in the input array `nums`:
   - If `num` is less than the pivot, append it to the `less` list.
   - If `num` is equal to the pivot, append it to the `equal` list.
   - If `num` is greater than the pivot, append it to the `greater` list.

3. **Rearrangement:**  After iterating through the entire array, concatenate the `less`, `equal`, and `greater` lists in that order to form the final rearranged array: `nums`. 

4. **Output:** Return the rearranged array `nums`.


## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the length of the input array `nums`
    *  The algorithm iterates through each element of the array once, resulting in a time complexity of O(N). 

* **Space Complexity:** $O(1)$
   * We are creating three lists with constant space complexity. The number of elements we create is independent of the input array's size, making it a constant amount of memory use.
