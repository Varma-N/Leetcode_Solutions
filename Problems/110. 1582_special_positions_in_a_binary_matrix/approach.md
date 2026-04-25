# Special Positions in a Binary Matrix

## Problem Description
Given an `m x n` binary matrix `mat`, return the number of special positions in the matrix.

A position `(i, j)` is called **special** if:
* `mat[i][j] == 1`
* All other elements in row `i` are `0`.
* All other elements in column `j` are `0`.

---

## Step-by-Step Approach

### 1. Identify the Requirement
A position is special only if it is the sole '1' in its entire row and the sole '1' in its entire column. This means we need a way to quickly check the count of '1's for any given row and column.

### 2. Pre-calculate Row and Column Sums
Instead of re-scanning the entire row and column for every '1' we encounter (which would be inefficient), we can pre-calculate the frequency of '1's:
* Create an array `row_count` where `row_count[i]` stores the number of '1's in the $i$-th row.
* Create an array `col_count` where `col_count[j]` stores the number of '1's in the $j$-th column.

### 3. Iterate Through the Matrix
Traverse each cell `(i, j)` of the matrix using nested loops.

### 4. Apply the Special Condition
For each cell `mat[i][j]`, check the following three conditions:
1.  Is the current element a '1'? (`mat[i][j] == 1`)
2.  Is it the only '1' in its row? (`row_count[i] == 1`)
3.  Is it the only '1' in its column? (`col_count[j] == 1`)

### 5. Count and Return
If all three conditions are met, increment a global counter. Once the traversal is complete, return the total count.

---

## Complexity Analysis

### Time Complexity: $O(m 	imes n)$
* **Preprocessing:** We iterate through the matrix once to calculate row and column sums, taking $O(m 	imes n)$ time.
* **Counting:** We iterate through the matrix a second time to check each cell against our pre-calculated sums, also taking $O(m 	imes n)$ time.
* Total time complexity is $O(m 	imes n)$, where $m$ is the number of rows and $n$ is the number of columns.

### Space Complexity: $O(m + n)$
* We use two auxiliary arrays to store the sums: one of size $m$ (for rows) and one of size $n$ (for columns).
* Total extra space used is proportional to the dimensions of the matrix, $O(m + n)$.
