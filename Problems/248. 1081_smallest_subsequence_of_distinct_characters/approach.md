## Approach

This problem can be efficiently solved using a **Monotonic Stack** along with a dictionary/array to keep track of the remaining characters. 

Here is the step-by-step approach:

1. **Find the Last Occurrence:** Iterate through the string `s` and record the last index at which each character appears. This helps us know if we can safely discard a character from our stack because we will encounter it again later.
2. **Initialize Data Structures:** 
   * A `stack` to build the lexicographically smallest subsequence.
   * A `visited` set (or boolean array) to keep track of the characters currently present in the stack, ensuring we only include each distinct character exactly once.
3. **Iterate Through the String:** Loop through each character `c` in the string `s` along with its index `i`.
4. **Skip Duplicates:** If the current character `c` is already in the `visited` set, simply ignore it and move to the next character.
5. **Maintain Lexicographical Order (Monotonic Stack):** 
   * Before pushing `c` to the stack, check if it is lexicographically smaller than the character at the top of the stack.
   * If `c` is smaller, and the character at the top of the stack appears again later in the string (i.e., its last recorded index is greater than the current index `i`), it is safe to remove the top character.
   * Pop the top character from the stack and remove it from the `visited` set. 
   * Repeat this popping process as long as the conditions are met.
6. **Add the Current Character:** Push the current character `c` onto the stack and add it to the `visited` set.
7. **Build the Result:** Once the loop finishes, the stack will contain the characters of the required subsequence in the correct order. Join the characters in the stack to form the final string and return it.

---

## Complexity Analysis

* **Time Complexity:** $O(N)$, where $N$ is the length of the string `s`. We iterate through the string a constant number of times. Each character is pushed and popped from the stack at most once, making the stack operations $O(N)$ in total.
* **Space Complexity:** $O(1)$ or $O(k)$ where $k$ is the size of the character set (26 for lowercase English letters). The stack and the visited set will store at most 26 characters, which requires constant extra space regardless of the length of the input string.