# Problem 3517: Smallest Palindromic Rearrangement I

## Intuition
The solution leverages the fact that palindromes are symmetrical and can be rearranged to form smaller palindromes. By counting the occurrences of each character and ensuring the resulting string is lexicographically smallest, we can determine the smallest palindromic rearrangement.

## Approach
1. **Character Count:** Create a `Counter` object `counts` to store the frequency of each character in the input string `s`. 

2. **Left Half Analysis:** Create an empty list `left_half` to store characters. Initialize `mid` to an empty string. Iterate through each lowercase English character:
    *  If the character exists in `counts` and its count is odd: 
        * Set `mid` to the character. This ensures that the smallest possible palindrome is formed with the character.
    *  Append the character to `left_half` with a count determined by the `counts` character.
3. **Palindrome Creation:** Join the characters of `left_half` to form the left half of the potential palindrome (`left_string`). 
4. **Rearrangement:**  Append the `mid` character and reverse the `left_string` ( `left_string[::-1]`) to form the final palindrome.

## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the length of the input string. 
    * The loop iterates over each character in `s`, and the `Counter` object has a time complexity of O(N) for counting.
* **Space Complexity:** $O(1)$ as the code only uses constant extra space for temporary storage and variable initialization.