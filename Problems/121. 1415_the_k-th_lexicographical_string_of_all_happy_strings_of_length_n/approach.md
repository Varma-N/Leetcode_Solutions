# Step-by-Step Approach: k-th Lexicographical Happy String

A **Happy String** is defined as a string that:
1. Consists only of characters from the set `['a', 'b', 'c']`.
2. Does not have the same character in any two consecutive positions (i.e., `s[i] != s[i+1]`).

## Problem Breakdown

The goal is to find the $k$-th lexicographically smallest happy string of length $n$. Instead of generating all possible strings (which would be $3 	imes 2^{n-1}$ strings), we use a mathematical approach to "jump" to the correct string.

---

## Step-by-Step Logic

### 1. Calculate Total Possibilities
The total number of happy strings of length $n$ can be calculated using the multiplication principle:
* **First Character:** We have **3** choices ('a', 'b', or 'c').
* **Subsequent Characters:** For every character after the first, we have **2** choices (any character from the set except the one used immediately before).
* **Total:** $3 	imes 2^{n-1}$.
* *Check:* If $k$ is greater than this total, return an empty string immediately.

### 2. Determine the String Character by Character
We build the string from left to right ($i = 0$ to $n-1$). At each position, we determine which character to pick by evaluating how many strings can be formed starting with that character.

#### A. Determine "Bucket Size"
For a given position $i$, if we pick a valid character, there are $n - 1 - i$ positions remaining. Each remaining position has exactly 2 choices. Therefore, the number of happy strings that share the current prefix is:
$$	ext{bucket\_size} = 2^{n-1-i}$$

#### B. Character Selection
We iterate through the available characters `['a', 'b', 'c']` in alphabetical order:
1.  **Check Validity:** Skip the character if it is the same as the character at index $i-1$ (to maintain the "happy" property).
2.  **Compare $k$ to Bucket Size:**
    * **If $k \le 	ext{bucket\_size}$:** This means the $k$-th string falls within the group of strings starting with the current character. We **append** this character to our result and move to the next position ($i+1$).
    * **If $k > 	ext{bucket\_size}$:** The $k$-th string is further down the lexicographical list. We **subtract** `bucket_size` from $k$ and try the next available character in the set.

### 3. Repeat until Length $n$
Continue this process until the string reaches length $n$. Since we checked the total count at the start, we are guaranteed to find a valid character for every position.

---

## Complexity Analysis

### Time Complexity: $O(n)$
* We iterate $n$ times (once for each character in the string).
* In each iteration, we check at most 3 characters.
* The total number of operations is proportional to the length of the string, making it $O(n)$.
* *Note:* The initial calculation of $2^{n-1}$ is $O(1)$ or $O(\log n)$ depending on the power implementation.

### Space Complexity: $O(n)$
* We store the result in a list/string of length $n$.
* The recursion stack (if using recursion) or the iterative storage is linear relative to $n$.
