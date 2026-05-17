# Approach

## Step 1: Initialize Variables
- Find the number of rows `n` and columns `m`.
- Define the modulo value `12345`.
- Create a result matrix `p` of size `n x m` initialized with `1`.

---

## Step 2: Compute Prefix Products
- Maintain a variable `prefix_prod` initialized as `1`.
- Traverse the grid from top-left to bottom-right.
- For every cell:
  - Store the current `prefix_prod` into `p[i][j]`.
  - Update `prefix_prod` by multiplying it with the current grid value.
  - Take modulo `12345` after multiplication.

This ensures that each cell stores the product of all elements appearing before it in traversal order.

---

## Step 3: Compute Suffix Products
- Maintain another variable `suffix_prod` initialized as `1`.
- Traverse the grid from bottom-right to top-left.
- For every cell:
  - Multiply the existing value in `p[i][j]` with `suffix_prod`.
  - Take modulo `12345`.
  - Update `suffix_prod` by multiplying it with the current grid value.
  - Again, apply modulo `12345`.

Now each cell contains:
- Product of all elements before it
- Multiplied by product of all elements after it

Thus, every position stores the product of all grid elements except itself.

---

# Time Complexity
- The grid is traversed twice.
- Each traversal takes `O(n * m)`.

**Overall Time Complexity:** `O(n * m)`

---

# Space Complexity
- The result matrix `p` uses extra space of size `n * m`.

**Overall Space Complexity:** `O(n * m)`
