# Problem 61: Rotate List

## Intuition
Rotating a linked list to the right by k places involves shifting the nodes in the list, effectively changing the order of elements.  The intuition lies in utilizing pointers and finding the last node. Then we iterate through the list and determine new head based on the position 'k'.


## Approach
1. **Determine the length of the linked list:** 
   - If the list is empty (`head` is None or `head.next` is None), return `head`.
   -  Iterate using a pointer `old_tail` to traverse the list, counting the number of nodes (`length`) until we encounter the end (`old_tail.next` is None). 

2. **Handle edge cases:** 
   - If `k == 0`, there's no rotation needed; return the original `head`.

3.  **Set `old_tail.next`:**
    - Connect the last node with `head`, starting point of the rotation process.
4.  **Calculate steps to new tail:**
   - Use modulo operation (`k % length`) to determine the actual position for rotation based on the value of 'k'. 

5. **Iterate and move to the new tail:**
   - Set `new_tail` to current node, which is initially `head`, and then traverse through the list using a loop until we reach the new tail (determined in step 4).
6.  **Set new head and remove old tail:** 
    - Finally, change the next pointer of the node following `new_tail` to `None`.


## Complexity Analysis
* **Time Complexity:** $O(N)$ 
    * The time complexity is determined by traversing the list once to find length and another loop to shift nodes.
* **Space Complexity:** $O(1)$ 
    * We use a constant amount of extra space during execution to store variables like `head`, `old_tail` and `new_tail`.