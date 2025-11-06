# 💡 Problem #3370: Smallest Number With All Set Bits
**Link:** [LeetCode #3370](https://leetcode.com/problems/smallest-number-with-all-set-bits/)

---

## 🧠 Approach

### 🔍 Problem Understanding
We are given an integer `n`.  
We need to find the **smallest number** that:
1. Has **all bits set to 1** in its binary form (like 1 → 1, 3 → 11, 7 → 111, 15 → 1111, etc.)
2. Is **greater than or equal to `n`**

---

### ⚙️ Intuition
Numbers with all bits set follow a clear binary pattern:

| Decimal | Binary |
|----------|---------|
| 1 | 1 |
| 3 | 11 |
| 7 | 111 |
| 15 | 1111 |
| 31 | 11111 |

So, the goal is to find the **smallest number from this pattern** that is **≥ n**.

---

### 🧩 Step-by-Step Reasoning

1. Start from `x = 1` (which is binary `1`).
2. As long as `x` is smaller than `n`, keep generating the next number in the pattern.
3. To generate the next number with all bits set:
   - Left shift `x` → this moves all bits one position left.
   - Then OR with `1` → this sets the new rightmost bit to 1.
   - Code representation:
     ```python
     x = (x << 1) | 1
     ```
4. Repeat this until `x >= n`.
5. Return `x` as the final answer.

---

### 🧮 Example Walkthrough

#### Example 1:
**Input:** `n = 6` 
```
x = 1 → binary 1
x = 3 → binary 11
x = 7 → binary 111 → 7 >= 6 → return 7
```

✅ Output: `7`

#### Example 2:
**Input:** `n = 10` 
```
x = 1 → 3 → 7 → 15 → 15 >= 10 → return 15
```

✅ Output: `15`

---

### 🧠 Why This Works
The pattern `(x << 1) | 1` effectively keeps appending `1`s to the binary representation of `x`.  
This ensures that `x` will always be of the form `111...1`, i.e., all bits set to 1.

---

### ⏱️ Time Complexity
- **O(log n)** → because each shift doubles `x` until it surpasses `n`.

### 💾 Space Complexity
- **O(1)** → uses only constant extra space.

---

✅ **Key Insight:**  
By continuously left-shifting and setting bits, we can efficiently reach the smallest “all-1s” number that’s ≥ `n`.
