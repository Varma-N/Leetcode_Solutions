# 💡 Problem #3234: Count the Number of Substrings With Dominant Ones
**Link:** https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

---

## 🧠 Problem Understanding

A substring is called **dominant** if:

(# of ones) ≥ (# of zeros)²


Given a binary string `s`, count how many substrings satisfy this condition.

---

## ⚙️ Key Insight

Let:
- `z = number of zeros` in the substring  
- `l = length of substring`

Since:

ones = l - z <br/>
Condition: (l - z) ≥ z² → l ≥ z + z²


### This implies:
- Substrings with **no zeros** (z = 0) are automatically valid.
- Substrings with **small z** can be processed via enumeration.
- Substrings with large z cannot ever satisfy the inequality because `z²` grows very fast.

Empirically, `z ≤ 200` is always safe for all constraints.

Thus we split the problem:

---

## ✔️ Case 1: z = 0 (all ones)

For each starting index `i`, the substring can extend up to the first zero.

Using a list of zero positions, we can count:

end_index = zero_pos[next_zero] - 1 <br/>
total += end_index - i + 1


---

## ✔️ Case 2: z = 1..Z_MAX (small number of zeros)

For fixed start `i` and fixed number `z`:

- Let the `z`-th zero from `i` be at position `last_zero`
- Minimal valid end index is:

min_end = max(last_zero, i + z + z² - 1)


- The substring must end **before the next (z+1)-th zero**, or at end of string:

max_end = zero_pos[p+z] - 1 (if exists) <br/>
or n-1


If:

min_end <= max_end

then all endpoints `min_end … max_end` produce valid substrings.

Add `(max_end - min_end + 1)` to the total.

---

## 🧠 Efficiency Explanation

We avoid checking every substring (which would be O(n²)).  
Instead:

- Zero positions allow us to jump over segments efficiently.
- Enumerating zeros up to 200 bounds the search.
- Each starting index `i` contributes in **amortized O(Z_MAX)**.

Total runtime:  
✔️ **O(n × Z_MAX)**  
with `Z_MAX = 200` → ~2e7 ops worst-case → fits easily.

---

## 🧩 Example

For `s = "110010"`:

- z = 0 substrings: count stretches of ones
- z = 1..200 substrings: enumerate using zero positions
- Build up total

---

## ⏱️ Complexity

- **Time:** `O(n × Z_MAX)`  
- **Space:** `O(n)` for zero positions

---

## 🔑 Key Insight

Dominant substrings can be counted by:
1. Tracking zero positions
2. Enumerating z = 0 separately
3. For z ≥ 1, deriving valid ranges for the end index using inequality constraints

This avoids brute-force while ensuring correctness.

