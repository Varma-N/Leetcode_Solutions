# Problem 2058: Find the Minimum and Maximum Number of Nodes Between Critical Points

## Intuition
The key to solving this problem is to first identify all the critical points in the linked list. A critical point is a node that has a value strictly greater than the previous node and the next node, or strictly smaller than the previous node and the next node. Once we have identified these critical points, we can determine the minimum and maximum distance between any two of them using the information from the previous nodes. 

## Approach
1. **Initialization:** 
    * `min_dis`:  Initialize with infinity (`float('inf')`) to store the minimum distance between two critical points. 
    * `critical_points`:  Initialize an empty list to store the indices of the critical points.
    * `res`: Initialize an empty list to store the answer (minimum distance and maximum distance).
    * `pos`: Initialize with 1 to keep track of the current node's position in the list.
    * `prev`: Initialize with the head of the list (`head`) to track the previous node.
    * `current`: Initialize with the next node of the head (`head.next`) to track the current node. 
2. **Iteration:** 
    * Loop through the list using `current`.
    * For each node: 
        * Check if the node's value fulfills the criteria for a critical point (is greater than the previous node and next node, or smaller than the previous node and next node). 
        * If the node is a critical point, append its position to the `critical_points` list. 
3. **Minimum and Maximum Distance:** 
    * If the list contains less than 2 critical points, return `[-1, -1]`.
    * If there are at least 2 critical points, calculate the distance between each pair of critical points. The distance is calculated by finding the difference between their positions in the list. 
4. **Return:** 
    * Return the list `res` containing the `min_dis` (minimum distance) and `max_dis` (maximum distance). 



## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The algorithm iterates through the linked list only once, with a linear time complexity. 
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of extra space regardless of the input size.