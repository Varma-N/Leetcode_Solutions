# Problem 3090: Maximum Length Substring With Two Occurrences

## Intuition
The key to solving this problem lies in using a sliding window approach to identify substrings with at most two occurrences of each character. We will maintain a dictionary `d` to track the count of each character within the sliding window. By constantly expanding the window and shrinking it when needed, we can find the maximum length of such a substring. 

## Approach
1. **Initialization**: 
    * `n`: Stores the length of the input string `s`.
    * `left, right`: Pointers representing the left and right edges of the sliding window, initialized to 0.
    * `d`: A dictionary to store the count of each character within the window. 
    * `max_length`: Stores the maximum length of a substring found so far, initialized to 0. 

2. **Sliding Window Expansion**:
    *  Iterate over the string `s` using the `right` pointer. 
        * For each character `s[right]`, increment its count in the dictionary `d` if it doesn't exist or increase its count by 1 if it exists.
    *  While the count of a character `s[right]` in the dictionary exceeds 2:
        * Decrease the count of the character at the left pointer `s[left]` in the dictionary `d` by 1.
        * Increment the left pointer `left` to shrink the window. 
    *  Calculate the length of the valid substring  `current_valid_substring_length` (the difference between `right` and `left`).
    *  Update `max_length` if the current substring length is greater than the previous `max_length`.

3. **Iteration & Return**: 
    *  Increment the `right` pointer to expand the window.  
    *  Continue the iteration until the right pointer reaches the end of the string. 
    *  Return `max_length`, the length of the substring with at most two occurrences of each character.

## Complexity Analysis
* **Time Complexity:** $O(N)$ 
    * We iterate through the string once (with the `right` pointer). 
* **Space Complexity:** $O(1)$ 
    *  The dictionary `d` has a constant space complexity since the size of the dictionary is independent of the input string length.