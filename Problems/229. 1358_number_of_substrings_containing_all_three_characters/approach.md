# Problem 1358: Number of Substrings Containing All Three Characters

## Intuition
The key to solving this problem is to understand the role of "windows" within the string. The window essentially represents a specific substring of the string that allows us to check for all three characters. The algorithm leverages this concept to identify and count the substrings containing all three characters.

## Approach
1. **Initialization:**
   - `left`: This variable keeps track of the starting index of the window. It serves as the left boundary of the window, starting from 0.
   - `total_count`: This variable stores the total number of substrings found, initialized to 0.
   - `window_counts`: This dictionary stores the frequency of each character within the current window, effectively counting how many of each character (a, b, c) are present within the window. 
   - `n`: Length of the input string.

2. **Sliding Window:**
   - The algorithm iterates through the string using a `for` loop with the `right` pointer, iterating through each character of the input string `s`.
   - **Character Count:** For each `char_right` (character at the `right` position), the `window_counts` dictionary is used to track the frequency of this character. It updates the count if it exists or initializes it to 0. 
   - **Window Evaluation:** 
     -  The loop continues as long as the number of unique characters in the `window_counts` dictionary (i.e., the window) is exactly equal to 3 (representing all three characters). 
     -  Within the `while` loop, the `total_count` is incremented by `n - right`, representing the substring length that meets the criteria. 
     - **Window Update:**  A left boundary is moved (`left += 1`) to update the window.  

3. **Result:** After traversing the string, the `total_count` stores the number of valid substrings.

## Complexity Analysis
* **Time Complexity:** $O(N)$, where N is the length of the string.  
    * The algorithm iterates through the string once, performing constant-time operations like accessing the dictionary. 
* **Space Complexity:** $O(N)$
    *  The dictionary used for `window_counts` stores a maximum of 3 unique characters at a time. The dictionary's size is proportional to the length of the string, thus its space complexity is $O(N)$.