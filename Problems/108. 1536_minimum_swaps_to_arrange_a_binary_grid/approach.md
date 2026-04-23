# Approach: Minimum Swaps to Arrange a Binary Grid

To solve this problem, we need to transform the binary grid into one where all elements above the main diagonal are zeros. This is equivalent to saying that for each row $i$ (where $i$ ranges from $0$ to $n-1$), the row must end with at least $n - 1 - i$ trailing zeros.

---

### Step-by-Step Approach

**1. Calculate Trailing Zeros**
The specific values in the grid don't matter as much as the count of consecutive zeros at the end of each row. 
* Iterate through each row of the $n \times n$ grid.
* Count how many zeros appear at the end of the row before hitting a $1$ or the beginning of the row.
* Store these counts in a list (e.g., `zeros = [count0, count1, ..., countN]`).

**2. Identify Requirements**
For the grid to satisfy the condition (all zeros above the main diagonal):
* Row $0$ needs at least $n - 1$ trailing zeros.
* Row $1$ needs at least $n - 2$ trailing zeros.
* Row $i$ needs at least $n - 1 - i$ trailing zeros.
* The last row (Row $n-1$) needs $0$ trailing zeros.

**3. Greedy Matching and Swapping**
We iterate through each position $i$ from $0$ to $n-1$ and find a valid row to place there:
* **Target:** For the current row $i$, we need a value in our `zeros` list that is $\ge (n - 1 - i)$.
* **Search:** Scan the `zeros` list starting from index $i$ to find the first row $j$ that satisfies the requirement.
* **Invalid Case:** If no such row is found between $i$ and $n-1$, it is impossible to satisfy the condition. Return `-1`.
* **Simulate Swap:** Once a valid row is found at index $j$:
    * The number of adjacent swaps needed to move this row to position $i$ is exactly $(j - i)$.
    * Add this distance to a running `swaps` counter.
    * Physically move the element in the list (or simulate the shift) so that the rows are reordered for the next iteration.

**4. Return Result**
After successfully placing a valid row for every position $i$, return the total `swaps` accumulated.

---

### Complexity Analysis

| Complexity | Notation | Reason |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n^2)$ | Calculating trailing zeros takes $O(n^2)$. The greedy matching loop runs $n$ times, and in each iteration, we may scan up to $n$ elements and perform a list shift (which is also $O(n)$). |
| **Space Complexity** | $O(n)$ | We store the count of trailing zeros for each row in a separate list of size $n$. |
