# 💡 Problem #2536: Increment Submatrices by One
**Link:** https://leetcode.com/problems/increment-submatrices-by-one/

---

## 🧠 Problem Understanding

You are given:
- An `n × n` matrix initialized to all **0**.
- A list of queries, each specifying a submatrix:
  
[r1, c1, r2, c2]


For each query, **increment every cell** inside that submatrix by **1**.

Instead of brute force (which is O(n² × q)), we need an optimal solution.

---

## ⚙️ Key Insight: 2D Difference Array

This problem is perfectly solved with a **2D difference matrix**, also called:
- *2D prefix difference*
- *Range update matrix*
- *Imos method (2D)*

### How it works:
To increment all cells in a submatrix `(r1,c1)` → `(r2,c2)`:

diff[r1][c1] += 1 <br/>
diff[r1][c2 + 1] -= 1 <br/>
diff[r2 + 1][c1] -= 1 <br/>
diff[r2 + 1][c2 + 1] += 1


After applying all updates, we restore the final matrix using:
1. Row-wise prefix sum
2. Column-wise prefix sum

This reconstructs the actual incremented matrix efficiently.

---

## 🧩 Step-by-Step Example

For a query affecting:

r1, c1 = 1, 1 <br/>
r2, c2 = 2, 2


Meaning we increment this 2×2 block:

(1,1) (1,2) <br/>
(2,1) (2,2)


We apply to diff:

diff[1][1] += 1 <br/>
diff[1][3] -= 1 <br/>
diff[3][1] -= 1 <br/>
diff[3][3] += 1 


After prefix sums, the effect propagates exactly inside the rectangle.

---

## 🧠 Why This Works
2D difference arrays allow us to apply each rectangle update in **constant time**, and after all updates, prefix sums reconstruct the final values.

Total cost:
- Processing q queries: **O(q)**
- Building final matrix: **O(n²)**

Much faster than applying each query individually.

---

## ⏱️ Complexity

- **Time:** O(n² + q)
- **Space:** O(n²)

---

## 🔑 Key Insight
Use a **2D difference matrix + prefix sums** to convert many rectangle updates into an efficient computation.
