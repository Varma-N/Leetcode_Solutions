# 1292. Maximum Side Length of a Square with Sum ≤ Threshold

## 🧠 Problem Summary
Given a 2D matrix `mat` and an integer `threshold`, return the **maximum side length** of a square submatrix such that the **sum of its elements is less than or equal to `threshold`**.

---

## 🚀 Approach (Prefix Sum + Binary Search)

### 1️⃣ Build Prefix Sum Matrix
To quickly compute the sum of any submatrix in **O(1)** time:

- Create a `(m+1) x (n+1)` prefix sum matrix `pre`
- Formula:

\[
pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
\]

This allows computing any `k × k` square sum in constant time.

---

### 2️⃣ Check if a Square of Size `k` Exists
For a given side length `k`:

- Iterate over all possible top-left positions
- Use prefix sum to compute square sum
- If any square has sum ≤ threshold → return `True`

Time for one check: **O(m × n)**

---

### 3️⃣ Binary Search on Side Length
- Minimum side length = `0`
- Maximum side length = `min(m, n)`
- Binary search to find the largest valid `k`

If square of size `mid` exists:
- Try bigger size (`left = mid + 1`)
Otherwise:
- Try smaller size (`right = mid - 1`)

---

## ⏱ Time Complexity

- Building prefix sum: **O(m × n)**
- Binary search: **O(log(min(m, n)))**
- Each check: **O(m × n)**

### ✅ Overall Time Complexity:
\[
O(m \times n \times \log(\min(m,n)))
\]

---

## 💾 Space Complexity

- Prefix sum matrix: **O(m × n)**

### ✅ Overall Space Complexity:
\[
O(m \times n)
\]

---

## 🎯 Key Takeaways

- Use **2D Prefix Sum** for fast submatrix sum queries.
- Use **Binary Search on Answer** when searching for maximum/minimum valid size.
- Efficient combination of both reduces brute-force complexity significantly.  
