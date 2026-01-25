# 💡 Problem #66: Plus One
**Link:** [Problem](https://leetcode.com/problems/plus-one/)

---

## 🧠 Problem Understanding

You are given a non-empty array `digits` representing a **non-negative integer**.

- Each element represents a single digit
- Digits are stored from **most significant to least significant**
- No leading zeroes are present

Your task is to **increment the number by one** and return the resulting digits array.

---

## ⚙️ Key Insight

This problem mimics **manual addition with carry**.

We start adding `1` from the **least significant digit** (rightmost):

- If the digit is `< 9`, increment it and stop
- If the digit is `9`, it becomes `0` and carries over to the next digit

---

## 🧩 Algorithm Strategy

1. Traverse the array from **right to left**
2. If `digits[i] < 9`:
   - Increment it
   - Return the array immediately
3. If `digits[i] == 9`:
   - Set it to `0`
   - Continue carrying
4. If all digits were `9`, we need an extra digit:
`[9,9,9] → [1,0,0,0]`

---

## 🧮 Example Walkthrough

### Example 1
```
digits = [1,2,3]
→ increment last digit
→ [1,2,4]
```

### Example 2
```
digits = [9]
→ 9 becomes 0, carry out
→ [1,0]
```

### Example 3
```
digits = [9,9,9]
→ all digits roll over
→ [1,0,0,0]
```

---

## 🧠 Why This Works

- Carry propagation is handled cleanly
- Early return avoids unnecessary work
- Handles all edge cases (single digit, all 9s)

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(1) (ignoring output array)

---

## 🔑 Key Insight  
Simulate elementary addition from right to left, handling carry exactly like manual arithmetic.
