# Balance a Binary Search Tree - Approach

## Problem Overview
Given the root of a binary search tree, return a balanced binary search tree with the same node values. A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

## Approach: In-order Traversal + Rebuild

### Step 1: Collect Nodes via In-order Traversal
- Perform an in-order traversal of the original BST
- Since in-order traversal of a BST yields nodes in sorted order, store all node references in a list
- This gives us a sorted array of tree nodes without creating new nodes (memory efficient)
```
Function: inorder(node)
├─ Base case: if node is null, return
├─ Recursively traverse left subtree: inorder(node.left)
├─ Append current node reference to nodes list
└─ Recursively traverse right subtree: inorder(node.right)
```

### Step 2: Build Balanced BST from Sorted Nodes
- Use a divide-and-conquer approach similar to binary search
- Select the middle element of the current range as the root of the subtree
- Recursively build left subtree from left half and right subtree from right half
- Reuse existing node objects by reassigning their left and right pointers
```
Function: build_balanced(left, right)
├─ Base case: if left > right, return null
├─ Calculate mid index: mid = (left + right) // 2
├─ Select nodes[mid] as current subtree root
├─ Recursively build left subtree: build_balanced(left, mid - 1)
├─ Recursively build right subtree: build_balanced(mid + 1, right)
└─ Return the root node
```

### Step 3: Return the New Root
- Call `build_balanced(0, len(nodes) - 1)` to construct the balanced tree
- Return the root node of the newly balanced BST

## Why This Works
1. **In-order property**: BST in-order traversal produces sorted sequence
2. **Middle element as root**: Choosing middle element ensures both subtrees have roughly equal height
3. **Recursive balance**: Applying this logic recursively guarantees O(log n) height
4. **Node reuse**: We modify pointers of existing nodes instead of creating new ones

## Edge Cases Handled
- Empty tree: Returns null
- Single node: Returns the same node
- Already balanced tree: Rebuilds with same structure (functionally equivalent)
- Completely skewed tree: Transforms into perfectly balanced tree

## Time Complexity
- **O(n)** where n is the number of nodes
  - In-order traversal: O(n)
  - Building balanced tree: O(n) - each node is visited exactly once
  - Overall: O(n) + O(n) = O(n)

## Space Complexity
- **O(n)** where n is the number of nodes
  - Storage for nodes list: O(n)
  - Recursion stack for in-order traversal: O(h) where h is tree height
  - Recursion stack for building: O(log n) for balanced result
  - Overall: O(n) dominated by the nodes list storage
