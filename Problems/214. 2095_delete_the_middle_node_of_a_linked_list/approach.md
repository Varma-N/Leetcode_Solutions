# Problem 2095: Delete the Middle Node of a Linked List

## Intuition
The middle node deletion problem can be efficiently solved using the "two-pointer" approach. By identifying the fast and slow pointers, we traverse the linked list while keeping the fast pointer two steps ahead from the slow pointer. When the fast pointer reaches the end (None), the slow pointer marks the middle node and the next pointer of the slow pointer becomes the new head of the modified linked list.

## Approach
1. **Initialization:**
   - `slow` pointer starts at the beginning of the linked list (`head`). 
   - `fast` pointer starts at the beginning of the linked list (`head`) as well.

2. **Two-Pointer Traversal:**
   - We move the `slow` pointer one node at a time while the `fast` pointer moves two nodes at a time. 
   - `prev` is used to store the previous value of the slow pointer for creating the new head of the modified linked list.

3. **Finding Middle Node:**
   - When the `fast` pointer reaches `None`, the `slow` pointer points to the middle node.


## Complexity Analysis
* **Time Complexity:** $O(N)$ 
    * We traverse the linked list using two pointers, and the time complexity of each step is O(1).

* **Space Complexity:** $O(1)$ 
    * The algorithm uses a constant amount of extra space.