# 💡 Problem #1526: Minimum Number of Increments on Subarrays to Form a Target Array
**Link:** [LeetCode #1526](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)

---

## 🧠 Approach

### 🔍 Problem Understanding
We are given an integer array `target`.  
Initially, we have an array of the same size filled with zeros.  
We can perform an operation where we **increment all elements of any chosen subarray by 1**.  

The goal is to find the **minimum number of such operations** required to make the array equal to `target`.

---

### ⚙️ Intuition
Think about how the values in the array grow from left to right.

- Every time we see an increase from `target[i-1]` to `target[i]`,  
  we must perform **additional operations** to raise elements up to the new height.

- If `target[i] <= target[i-1]`, no new operations are needed since previous increments already covered it.

So, the number of operations equals:
- `target[0]` (for the first element)
- Plus the sum of all **positive increases** `(target[i] - target[i-1])`

---

### 🧩 Step-by-Step Example

#### Example:
**Input:** `target = [1, 2, 3, 2, 1]`
```
operations = target[0] = 1

i = 1 → 2 > 1 → +1 operation (total 2)
i = 2 → 3 > 2 → +1 operation (total 3)
i = 3 → 2 < 3 → +0 operation (total 3)
i = 4 → 1 < 2 → +0 operation (total 3)
```

✅ Output: `3`

Explanation:  
- Increment subarray `[0:3]` three times → [1,2,3,3,3]
- Then decrease naturally as values are already covered by previous operations.

---

### 🧠 Why This Works
Each **increase** from `target[i-1]` to `target[i]` represents the need for **new independent operations** that can’t be merged with previous ones.

Thus, the minimal total number of operations is the **sum of all positive increases**.

---

### ⏱️ Time Complexity
- **O(n)** → One pass through the array.

### 💾 Space Complexity
- **O(1)** → Only a few variables used.

---

✅ **Key Insight:**  
Focus only on *increases* between consecutive elements — that’s where new work (operations) must happen.


