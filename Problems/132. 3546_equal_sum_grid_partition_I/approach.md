# 3546. Equal Sum Grid Partition I - Approach

## Step-by-Step Approach

**Step 1: Calculate the Total Sum**
First, calculate the sum of all the elements present in the `m x n` matrix. Let's call this `total_sum`.

**Step 2: Parity Check**
Before checking any partitions, check if `total_sum` is an odd number. Since the grid contains only positive integers, it is impossible to divide an odd total sum into two equal integer halves. If `total_sum % 2 != 0`, immediately return `false`.

**Step 3: Evaluate Horizontal Cuts**
A horizontal cut divides the matrix between two adjacent rows. To find if a valid horizontal cut exists:
1. Initialize a `prefix_sum` variable to `0`.
2. Iterate through each row of the matrix from the top to the second-to-last row (index `0` to `m-2`). We stop before the last row because both resulting sections (top and bottom) must be non-empty.
3. For each row, add the sum of its elements to `prefix_sum`.
4. After adding a row's sum, check if `prefix_sum * 2 == total_sum` (which is equivalent to checking if `prefix_sum == total_sum / 2`). If it matches, a valid horizontal partition exists. Return `true`.

**Step 4: Evaluate Vertical Cuts**
If no valid horizontal cut is found, proceed to evaluate vertical cuts, which divide the matrix between two adjacent columns:
1. Reset the `prefix_sum` variable to `0`.
2. Iterate through each column from the left to the second-to-last column (index `0` to `n-2`). We stop before the last column to ensure both resulting sections (left and right) are non-empty.
3. For each column, calculate the sum of its elements across all rows and add it to `prefix_sum`.
4. Check if `prefix_sum * 2 == total_sum`. If it matches, a valid vertical partition exists. Return `true`.

**Step 5: Final Conclusion**
If all possible horizontal and vertical cuts have been evaluated and none result in equal sums, it is impossible to partition the grid as required. Return `false`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(m \times n)$
  * Calculating the `total_sum` requires visiting every element in the matrix once, taking $\mathcal{O}(m \times n)$ time.
  * Checking horizontal cuts involves calculating row sums, which takes at most $\mathcal{O}(m \times n)$ time.
  * Checking vertical cuts involves calculating column sums, taking at most $\mathcal{O}(m \times n)$ time.
  * Therefore, the overall time complexity is linear with respect to the number of elements in the grid, $\mathcal{O}(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns.
  
* **Space Complexity:** $\mathcal{O}(1)$
  * The algorithm only utilizes a few scalar variables (such as `total_sum` and `prefix_sum`) to maintain a running total. It does not require any additional arrays, matrices, or data structures that scale with the input size. Thus, the auxiliary space complexity is constant, $\mathcal{O}(1)$.
