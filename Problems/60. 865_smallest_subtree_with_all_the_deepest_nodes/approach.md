# Smallest Subtree with all the Deepest Nodes (LeetCode 865)

## Intuition

We want the **smallest subtree** that contains **all the deepest nodes** in a binary tree.

Key observations:
- The deepest nodes are those at the **maximum depth** of the tree.
- The smallest subtree containing all of them is essentially their **lowest common ancestor (LCA)**.
- If deepest nodes exist in **both left and right subtrees**, the current node is the answer.
- If they exist only in one subtree, the answer lies **entirely in that subtree**.

---

## Step-by-Step Approach

1. Use **postorder DFS** (process left, right, then node).
2. For each node, return **two values**:
   - `depth`: the maximum depth of the subtree rooted at this node
   - `candidate`: the node that is the root of the smallest subtree containing all deepest nodes in this subtree
3. Recursively compute results for left and right children.
4. Compare left and right depths:
   - If `left_depth > right_depth`  
     → deepest nodes are only in the left subtree  
     → return `(left_depth + 1, left_candidate)`
   - If `right_depth > left_depth`  
     → deepest nodes are only in the right subtree  
     → return `(right_depth + 1, right_candidate)`
   - If `left_depth == right_depth`  
     → deepest nodes exist in both subtrees  
     → current node is their LCA  
     → return `(left_depth + 1, current_node)`
5. The final answer is the `candidate` returned from the root.

---

## Why This Works

- Depth information flows **bottom-up**.
- The moment both subtrees have the same maximum depth, we’ve found the **lowest node** that covers all deepest nodes.
- Each node is visited **once**, and decisions are made locally.

---

## Time Complexity

- **Time:** `O(n)`  
  Each node is visited exactly once.
- **Space:** `O(h)`  
  Due to recursion stack, where `h` is the height of the tree (`O(n)` worst-case, `O(log n)` for balanced trees).
