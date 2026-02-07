# 1339. Maximum Product of Splitted Binary Tree

## Problem Summary

You are given a binary tree where each node contains an integer value.  
You must remove **exactly one edge** from the tree, splitting it into two subtrees.

The objective is to **maximize the product of the sums** of the values in these two subtrees.  
Since the result can be large, return it modulo **10⁹ + 7**.

---

## Core Idea

If the total sum of the entire tree is `T`, and removing an edge creates a subtree with sum `S`, then:
`Product = S × (T − S)`

So the problem becomes:
- Compute the total sum of the tree
- Consider every subtree as a potential split
- Track the maximum possible product

---

## Step-by-Step Approach

### 1. Compute the Total Sum of the Tree

Traverse the entire tree once using DFS to calculate the total sum of all node values.

This value remains fixed and is used to determine the complementary subtree sum after any split.

---

### 2. Compute Subtree Sums and Evaluate Splits

Perform another DFS traversal where:
- Each node calculates the sum of its own subtree
- Treat the edge above the current subtree as the cut
- Compute the product of:
  - the current subtree sum
  - the remaining tree sum (`total_sum - subtree_sum`)
- Update the maximum product encountered

Every possible split is evaluated during this traversal.

---

### 3. Return the Final Answer

After processing all nodes:
- Return the maximum product found
- Apply modulo **10⁹ + 7** to the result

---

## Time Complexity

- **O(N)**  
  Each node is visited twice (once for total sum, once for subtree evaluation)

---

## Space Complexity

- **O(H)**  
  Due to recursion stack in DFS  
  - Best case (balanced tree): `O(log N)`
  - Worst case (skewed tree): `O(N)`

---

## Key Takeaways

- The optimal split always corresponds to cutting at some subtree boundary
- Evaluating all subtree sums guarantees the maximum product
- Two DFS traversals ensure both clarity and efficiency

This approach is optimal and fits well within the problem constraints.
