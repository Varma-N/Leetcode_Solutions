# Problem 2265: Count Nodes Equal to Average of Subtree

## Intuition
To determine if a node's value equals the average of its subtree, we need two pieces of information for every node: the sum of all values in its subtree and the total number of nodes in that subtree. Since a parent node relies on the data from its children to calculate its own subtree sum and count, a bottom-up approach using post-order traversal is the most efficient way to solve this.

## Approach
1. **Initialization:**
   - `self.matching_nodes = 0`: Initialize a variable to keep track of the total number of nodes that satisfy the condition.

2. **Recursive Calculation (Post-Order Traversal):**
   - Create a helper function `post_order(node)` that traverses the tree and returns a tuple `(sum, count)` for the current subtree.
   - **Base Case:** If the current node is null, return `(0, 0)` since an empty tree has a sum of 0 and a count of 0.
   - **Traverse Children:** Recursively call `post_order` on `node.left` and `node.right` to retrieve the sums and counts of the left and right subtrees.
   - **Process Current Node:** 
     - Calculate `curr_sum` by adding `node.val` to the sums of both child subtrees.
     - Calculate `curr_count` by adding 1 (for the current node) to the node counts of both child subtrees.
   - **Evaluate Condition:** Check if the integer division of `curr_sum // curr_count` is equal to `node.val`. If it matches, increment `self.matching_nodes` by 1.
   - **Return to Parent:** Return `(curr_sum, curr_count)` so the parent node can use these values for its own calculations.

3. **Return:**
   - Initiate the recursive traversal by calling `post_order(root)`.
   - `return self.matching_nodes`: Return the final count of nodes that met the criteria.

## Complexity Analysis
- **Time Complexity:** $O(n)$
    * The algorithm uses a single post-order traversal, meaning it visits each node in the binary tree exactly once. Calculating the sum, count, and average takes constant time at each step, resulting in a time complexity of $O(n)$, where $n$ is the number of nodes.
- **Space Complexity:** $O(h)$
    * The space complexity is determined by the maximum depth of the recursive call stack, which corresponds to the height of the tree $h$. In a balanced tree, this is $O(\log n)$, but in the worst-case scenario (a completely skewed tree), the space complexity becomes $O(n)$.