# 💡 Problem #1930: Unique Length-3 Palindromic Subsequences
**Link:** https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

---

## 🧠 Problem Understanding

A **length-3 palindromic subsequence** has the form:
`a_a`
Where:
- The first and last characters are the same.
- The middle character can be anything.

The task is to count **unique** palindromic subsequences of this exact structure.

---

## ⚙️ Key Insight

For each character `a` from `'a'` to `'z'`:

1. Find:
   - `first = first occurrence index of a`
   - `last  = last occurrence index of a`
2. For the subsequence to exist:
`first < last`
3. The middle character can be **any distinct char** appearing between:
`s[first+1 ...last-1]`
4. Therefore: number of unique palindromes of form a?a
`= count(distinct chars in between)`

Repeat this for all 26 letters.

---

## 🧩 Example

`s = "aabca"`

- For `'a'`:
- First = 0
- Last = 4
- Middle substring = `"abc"` → distinct chars = {a, b, c}
→ contributes **3**: `aba`, `aca`, `aaa`

- For `'b'`:
- No valid pair → contributes 0

- For `'c'`:
- No valid pair → contributes 0

Total answer = **3**

---

## 🧠 Why This Works

- We only need to consider 26 characters → constant overhead.
- Checking first and last occurrence is O(n).
- Using a set to count middle distinct characters is efficient.

This gives us a **clean O(26 × n)** = **O(n)** solution.

---

## ⏱️ Time Complexity
- `O(n)` to scan string for each character (26), but effectively linear
- So **O(n)**

## 💾 Space Complexity
- Set of at most 26 characters → **O(1)**

---

## 🔑 Key Insight  
A length-3 palindrome is fully determined by:
- The outer character  
- The distinct characters appearing between its first and last occurrence.
