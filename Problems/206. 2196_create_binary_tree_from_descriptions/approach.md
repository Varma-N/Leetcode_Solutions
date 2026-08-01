# Problem 2196: Create Binary Tree From Descriptions

## Intuition
The solution creates a binary tree by traversing the input descriptions array. Each description indicates which node is the parent and if it's left or right child. By mapping each node to a `TreeNode` object, we build the tree structure based on the relationships defined in the `descriptions`.  A "left" child is created if `isLefti == 1`, otherwise, it's a "right" child (`isLefti == 0`). The algorithm uses a hash map (`nodes`) to efficiently store nodes and check for their existence before building the tree.

## Approach
1. **Initialization:**
   - Create an empty dictionary `nodes` that will store each node in the tree as a key (parent/child).
   - Create an empty set `children` to keep track of all children encountered during the traversal.

2. **Traversal and Construction:** 
    - For each description `[parenti, childi, isLefti]` in `descriptions`:
        - If `parenti` doesn't exist in `nodes`, create a new `TreeNode` object for it. 
        - If `childi` doesn't exist in `nodes`, create a new `TreeNode` object for it. 
    - If `isLefti == 1`:  Set the left child of `parenti` to `childi`. 
    - Otherwise, set the right child of `parenti` to `childi` (`isLefti == 0`).
   - Add `childi` to the `children` set.
3. **Validating the Tree:**
   - Iterate through the descriptions one last time, checking if each node exists in the `children` set and returns null when none of the nodes are found.

4.  **Return Root:** Return the root of the tree if it was created successfully. Otherwise, return `None`.


## Complexity Analysis 
* **Time Complexity:** $O(N)$
    - We traverse the descriptions array once, resulting in O(N) time complexity.
* **Space Complexity:** $O(1)$
    - The number of nodes created is proportional to the length of the input array.  The space used for storing data structures like `nodes` and `children` remains constant.

```
