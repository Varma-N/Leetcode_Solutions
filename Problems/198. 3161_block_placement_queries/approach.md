# Problem 3161: Block Placement Queries

## Intuition
The solution leverages a binary tree data structure to represent obstacles on the infinite line, allowing efficient query and update operations. This approach facilitates a fast check for block placement based on their size and range constraints. 


## Approach
**1. Data Structure:** A binary tree is employed to store information about obstacles. Each node in the tree represents a segment of the line and holds:

   - **has_obs:** Indicates whether an obstacle exists at that segment (True if present, False otherwise).
   - **first_obs, last_obs:** Represent the starting and ending points of the obstacle within the segment. 
   - **max_gap:**  Specifies the maximum distance between any two adjacent obstacles in the same segment.

**2. Query Processing (`query(node, start, end, l, r)`)**:

   - The `query` function takes a node in the tree and queries for blocks within a specific range on the line.
    - **Tree Exploration:** It recursively traverses the tree based on query bounds, utilizing the `first_obs`, `last_obs`, and `max_gap` properties of nodes to determine if there is an obstacle or not. 
    - **Merge Operations:** The function uses `merge` to combine results from subtrees representing potential blocks, ensuring accuracy in determining block placement possibilities.

**3. Building the Tree (`build(node, start, end)`)**:
  - This function constructs the binary tree structure, segment by segment. 
   -  It recursively divides the line segment into smaller segments (sub-segments), creating nodes for each sub-segment to store information about obstacles within them.


**4. Update Operation (`update(node, start, end, pos)`)**:
   -  This function updates an obstacle by modifying the corresponding node in the binary tree, and ensuring consistency with the updated segment boundaries. 
  
## Complexity Analysis

* **Time Complexity:** $O(N \log N)$ for constructing the tree. This is because we are dividing the line into sub segments recursively, each of which needs to be stored in the tree. Then, during queries and updates, the time complexity becomes $O(\log N)$. 
    -  `build(1, 0, M)` creates a binary tree for the input range, resulting in O(M) operations.
    -  `query(1, 0, M, 0, x)` performs a specific query on a node.
* **Space Complexity:** $O(N)$ 

   - The space complexity is determined by the number of nodes in the tree (which grows linearly with the input size). 



```
