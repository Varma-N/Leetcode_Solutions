# Problem Logic: Check If a String Contains All Binary Codes of Size K

## 1. Define the Goal
To return `true` if every possible binary code of length `k` is present as a substring in the given string `s`. Otherwise, return `false`.

---

## 2. Step-by-Step Approach

### Step A: Determine the Target Count
Since binary codes consist of `0`s and `1`s, the total number of unique combinations for a length `k` is $2^k$.
* **Logic:** You can calculate this using `2 ** k` or the bitwise shift `1 << k`.
* **Example:** If $k = 2$, the codes are `00, 01, 10, 11`. You need to find $2^2 = 4$ unique strings.

### Step B: The "Impossible" Check (Optimization)
Before looping, check if the string `s` is even long enough to contain all unique codes. 
* **Logic:** There are $2^k$ codes, and each starts at a unique index. If the number of possible starting positions in `s` is less than the number of codes required, return `False` immediately.

### Step C: Track Unique Substrings
Use a **Set** data structure to store the unique substrings encountered. Sets are ideal here because they automatically handle duplicates, and checking the size of a set is an $O(1)$ operation.

### Step D: The Sliding Window
Iterate through the string `s` using a window of size `k`.
1.  **Extract:** Take the substring from current index `i` to `i + k`.
2.  **Store:** Add that substring to your Set.
3.  **Early Exit:** After adding a code, check if the size of the Set equals your target count ($2^k$). If it does, you can return `True` immediately without finishing the loop.



### Step E: Final Verdict
If the loop finishes and the Set size is still less than $2^k$, it means at least one binary code was missing from the string. Return `False`.

---

## 3. Complexity Analysis

### Time Complexity: $O(N \cdot k)$
* We traverse the string `s` of length $N$ once.
* In each iteration, extracting a substring of length `k` and hashing it to add to the Set takes $O(k)$ time.
* Therefore, the total time is $O((N - k) \cdot k)$, which simplifies to $O(N \cdot k)$.

### Space Complexity: $O(2^k \cdot k)$
* The Set can store up to $2^k$ unique strings.
* Each string stored in the Set has a length of `k`.
* This results in a total space requirement of $O(2^k \cdot k)$.
