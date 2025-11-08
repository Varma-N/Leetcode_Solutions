# 💡 Problem #3289: The Two Sneaky Numbers of Digitville
**Link:** [LeetCode #3289](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)

---

## 🧠 Approach

### 🔍 Problem Understanding
We are given an integer array `nums` that contains:
- Each number in the range `[0, n - 1]`
- Exactly **two numbers** that appear **twice**

We need to **return those two repeating numbers** in any order.

---

### ⚙️ Intuition
Since only two numbers appear twice, we can simply track what we've seen:
1. Initialize an empty `set()` to store unique numbers.
2. Iterate through `nums`:
   - If the number hasn’t been seen → add it to the set.
   - If the number is already in the set → it’s a duplicate, so append it to the result list.
3. Return the result list at the end.

---

### 🧩 Step-by-Step Example

#### Example:
**Input:** `nums = [0, 1, 1, 0]`

**Walkthrough:**
```
seen = {}
res = []

i = 0 → not in seen → add 0 → seen = {0}
i = 1 → not in seen → add 1 → seen = {0, 1}
i = 1 → in seen → res = [1]
i = 0 → in seen → res = [1, 0]
```


✅ **Output:** `[1, 0]`

---

### 🧠 Why This Works
- Using a set ensures constant-time lookups.  
- Since there are only two duplicates, we’ll end up adding exactly two elements to the result list.

---

### ⏱️ Time Complexity
- **O(n)** — we scan through the list once.

### 💾 Space Complexity
- **O(n)** — for the `set` used to track seen elements.

---

✅ **Key Insight:**  
Simple use of a hash set cleanly identifies duplicates without extra sorting or counting.
