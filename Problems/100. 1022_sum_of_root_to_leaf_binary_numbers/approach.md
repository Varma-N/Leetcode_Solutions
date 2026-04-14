# Sum of Root To Leaf Binary Numbers - Step-by-Step Approach

## Algorithm Steps

### 1. Initialize Depth First Search (DFS)
Begin a traversal starting from the root of the tree. Maintain a running total (`current_val`) that represents the binary number formed by the path from the root to the current node.

### 2. Handle the Null Case
If the current node is null, return 0. This ensures that empty branches do not contribute to the final sum.

### 3. Update the Path Value
Convert the path into a numerical value using bitwise operations. To append the current node's value (0 or 1) to the binary sequence:
* Shift the existing `current_val` to the left by 1 bit (equivalent to multiplying by 2).
* Perform a bitwise **OR** operation (or simple addition) with the current node's value.

### 4. Check for Leaf Nodes
Determine if the current node is a leaf (a node with no left or right children). If it is a leaf, the path is complete; return the `current_val`.

### 5. Recursive Exploration
If the node is not a leaf:
* Recursively call the DFS function for the left child.
* Recursively call the DFS function for the right child.
* Pass the updated `current_val` down to both children.

### 6. Aggregate Results
Sum the values returned from the left and right subtrees and return this total up the call stack.

---

## Complexity Analysis

* **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. We visit every node exactly once during the traversal.
* **Space Complexity:** $O(H)$, where $H$ is the height of the tree. This space is consumed by the recursion stack. In the worst case (a skewed tree), this could be $O(N)$; in a balanced tree, it would be $O(\log N)$.
