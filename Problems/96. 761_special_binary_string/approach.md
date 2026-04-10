# 761. Special Binary String - Approach

### Problem Overview
A **Special Binary String** is defined by two properties:
1. The number of `0`s is equal to the number of `1`s.
2. For every prefix, the number of `1`s is greater than or equal to the number of `0`s.

This definition is identical to **Valid Parentheses**, where `1` is an opening bracket `(` and `0` is a closing bracket `)`. The goal is to make the string lexicographically largest by swapping adjacent special substrings.

---

### Step-by-Step Approach

#### 1. Identification of Sub-problems
Because a special string can be composed of multiple smaller special strings, this problem has an **optimal substructure**. Think of the string as a collection of "mountain peaks" that are themselves special. To maximize the whole string, you must maximize each peak and then arrange the peaks in the best order.

#### 2. Splitting the String (Decomposition)
Traverse the string and maintain a `balance` counter (increment for `1`, decrement for `0`). 
- Whenever the `balance` hits `0`, you have identified a **minimal (primitive) special substring**.
- A primitive special substring is one that cannot be further split into two special substrings without breaking the "special" rules.

#### 3. Recursive Processing
A minimal special substring always starts with `1` and ends with `0`.
- To find the largest version of the string, you must look **inside** these boundaries.
- Take the inner part (the part between the first `1` and the last `0`) and recursively apply the same sorting logic.
- **Construction:** The processed result for that segment is `1` + `makeLargestSpecial(inner_part)` + `0`.

#### 4. Lexicographical Sorting
Once all primitive special substrings at the current level are collected into a list and recursively optimized:
- Sort the list of substrings in **descending order**.
- Lexicographically, `1100` (representing `(())`) is greater than `1010` (representing `()()`). Sorting descending ensures that the most "heavily nested" or "1-heavy" strings move to the front.

#### 5. Recombination
Join the sorted list of strings together. This local maximum contributes to the global maximum as the recursion unwinds.

---

### Key Intuition: The Parentheses Analogy
Think of `1` as `(` and `0` as `)`. 
- Input: `11011000` → `(())` and `(())`? No, the balance only hits zero at the end.
- The inner part of `1(101100)0` is `101100`.
- Recursively sorting the inner parts ensures that a string like `()(())` becomes `(())()`.

---

### Complexity Analysis

#### Time Complexity: $O(N^2)$
- **Splitting:** We traverse the string of length $N$ to find partitions, which is $O(N)$.
- **Sorting:** Sorting $K$ substrings takes $O(K \log K)$, but string comparisons in Python (and most languages) take $O(N)$.
- **Total:** In the worst case (highly nested strings), the recursion and sorting combine to $O(N^2)$.

#### Space Complexity: $O(N^2)$
- **Recursion Depth:** The stack depth can reach $O(N)$ in a deeply nested string (e.g., `111...000`).
- **Intermediate Storage:** In each recursive call, we create new substrings. Summing these across the recursion tree results in $O(N^2)$ space in the worst case.
