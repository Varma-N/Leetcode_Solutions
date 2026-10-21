# Problem 3720: Lexicographically Smallest Permutation Greater Than Target

## Intuition
The solution leverages the concept of lexicographical order and frequency counting to determine the lexicographically smallest permutation greater than the given target string. It starts by analyzing the target string and determining the character frequencies that need to be replaced with a lexicographically larger character. The algorithm iteratively builds the permutation by exploring the remaining character frequencies and finding the smallest character that satisfies the condition. 

## Approach
1. **Counting Character Frequencies:** Create a `Counter` object to store the frequency of each character in the input string `s`.
2. **Backtracking:**  Iterate through `s` in reverse order. For each character in `s`, check if the required character counts for the current prefix of `target` are satisfied. If not, continue to the next character.
3. **Building the Permutation:**  If the current prefix is valid, determine the lexicographically smallest character that meets the criteria. This character is then appended to the result string. 
4. **Generating Permutations:**  For each character that satisfies the lexicographical condition, append it to the result string. 
5. **Returning Result:** Return the lexicographically smallest permutation of `s` that is greater than `target`.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The algorithm iterates through `s` in reverse order, performing a constant amount of operations in each iteration. 
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of extra space, independent of the input size.