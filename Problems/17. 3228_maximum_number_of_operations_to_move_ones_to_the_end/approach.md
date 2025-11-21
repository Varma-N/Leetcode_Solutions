# 💡 Problem #3228: Maximum Number of Operations to Move Ones to the End
**Link:** https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

---

## 🧠 Problem Understanding

You are given a binary string `s`.  
You may perform the following operation any number of times:

- Choose an index `i` where `s[i] == '1'` and `s[i+1] == '0'`
- Swap the characters: `"10" → "01"`

Goal: **maximize** the number of operations performed before the string becomes stable.

---

## ⚙️ Key Insight

Each `"10"` swap effectively **moves a `1` to the right**, one position at a time.

The key observation is:

### ➤ Every time a `"1"` encounters a `"0"` to its right,  
the number of operations contributed is **equal to how many `1`s we have seen so far**.

Because:
- Each earlier `1` can also "push" behind this `0` in later steps.
- The order of operations doesn't matter — the total count is deterministic.

---

## 🧩 Logic Breakdown

We iterate through the string:

- Maintain `ones_count`: number of `1`s seen so far.
- When we see `'1'` at index `i`, increment `ones_count`.
- If `s[i] == '1'` and next char is `0`, this `"10"` pair contributes:
  
operations += ones_count

Why?
- All previously seen `1`s can pass through this specific `0` before it moves away.

---

## 🧮 Example

`s = "110010"`

Traverse step-by-step:

```
i=0 → '1' → ones=1
i=1 → '1' → ones=2
i=2 → '0'
i=3 → '0'
i=4 → '1' → ones=3 and next is '0'
→ operations += 3
```

Total operations = **3**

---

## ⏱️ Complexity

- **O(n)** time — single pass over the string.
- **O(1)** space.

---

## 🔑 Key Insight  
Every `"10"` boundary contributes as many operations as the count of `1`s before it.
