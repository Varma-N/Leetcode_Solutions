# 💡 Problem #2654: Minimum Number of Operations to Make All Array Elements Equal to 1
**Link:** https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

---

## 🧠 Problem Understanding

You are allowed to pick **two adjacent elements** and replace one of them with their **GCD**.  
Your goal is to make **all elements equal to 1** in the minimum number of operations.

Key fact:
- You can turn more elements into `1` only if somewhere in the array we can generate a `1` using GCDs.
- Since `gcd(x, y)` is always ≤ min(x, y), values decrease gradually.

---

## ⚙️ Key Observations

### 1️⃣ If the array already contains some `1`s  
Each `1` can help make its neighbors become `1`.

- If there are `ones` number of `1`s:  
  **Answer = n - ones**

Because each non-1 can be connected to the nearest `1`.

---

### 2️⃣ If there are *no* `1`s in the array  
We must **create** a `1` using GCD operations.

This is possible **only if the total gcd of the entire array is 1**:

(n - 1) more operations


So total = 
```
(L - 1) + (n - 1) = L + n - 2
```

We try all windows and take the minimum `L`.

---

## 🧩 Example

```
nums = [2,4,6,3]

No 1's present.
Total GCD = 1 → possible.

Smallest subarray with gcd = 1 is [6,3], length 2.

Answer = 2 + 4 - 2 = 4.
```

---

## ⏱️ Complexity

- Computing total gcd: **O(n)**
- Double loop to find smallest subarray with gcd = 1: **O(n²)** worst-case
- Space: **O(1)**

---

## 🔑 Key Insight  
If the array has no `1`s, the first step is the **hard part** — finding the minimal GCD segment that can generate the first `1`. After that, the rest is linear.
