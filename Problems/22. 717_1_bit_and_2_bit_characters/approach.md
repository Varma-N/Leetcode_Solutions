# 💡 Problem #717: 1-bit and 2-bit Characters
**Link:** https://leetcode.com/problems/1-bit-and-2-bit-characters/

---

## 🧠 Problem Understanding

You are given an array `bits` representing encoded characters:

- A **1-bit character** is represented by:  
  `0`
- A **2-bit character** is represented by:  
  `10` or `11`

The encoding must be parsed sequentially from left to right.  
The question is:

👉 **Does the last character consist of exactly one bit?**

---

## ⚙️ Key Insight

The parsing rules enforce:

- If we see a `0` → move forward by 1.
- If we see a `1` → this must start a 2-bit character → move forward by 2.

We only stop early if we jump exactly to the last index.

Thus:
- If traversal ends exactly at index `n-1`, the last char is 1-bit.
- If traversal jumps past it (or ends earlier), then the last char is part of a 2-bit sequence.

---

## 🧩 Example

### Example 1:

```
bits = [1, 0, 0]
Traverse:
i=0 → bits[0]=1 → jump 2 → i=2

i == n-1 → True
```

Answer: **True**

### Example 2:
```
bits = [1,1,1,0]
Traverse:
i=0 → jump 2 → i=2
i=2 → jump 2 → i=4 → out of bounds

i != n-1 → False
```

Answer: **False**

---

## 🧱 Why This Works

- The encoding rules allow **only one valid parsing path**.  
- We simulate that path and determine whether the last bit stands alone.  
- No DP or complex logic is needed.

---

## ⏱️ Complexity

- **Time:** O(n) — single scan  
- **Space:** O(1) — no extra memory

---

## 🔑 Key Insight  
Simulation of the decoding process directly answers whether the final bit forms a single-bit character.
