# Problem 3121: Count the Number of Special Characters II

## Intuition
A special character is defined as a letter that appears both in lowercase and uppercase within the input string. This can be achieved by identifying unique lowercase characters encountered earlier than any uppercase counterpart in the string. We count these unique letters to determine the total number of special characters. 


## Approach
1. **Initialization:** 
    *  `last_lower`: A dictionary to store the index of the last occurrence of a lowercase character encountered.
    * `first_upper`: A dictionary to store the index of the first occurrence of an uppercase character encountered.

2. **Iteration:**
    * Iterate through each character in the string using `enumerate(word)`. 
    * For every lowercase character:
        *  Add its index to `last_lower` dictionary with the character as the key. 
    * For every uppercase character: 
        * If it's not already present in `first_upper`, add its index and mark the presence of the character in `first_upper`.

3. **Counting Special Characters:**
    *  Iterate through each `last_lower` key-value pair, representing a unique lowercase character encountered earlier than any corresponding uppercase character. 
    * For every such character:
        * Look for its uppercase counterpart in `first_upper`.
        * If the last seen index is lower than the first appearance index of the corresponding uppercased letter in `first_upper`, increment the `count` by 1.

4. **Return:** Return the final `count`, representing the total number of special characters in the input string.


## Complexity Analysis
* **Time Complexity:** $O(N)$ -  The time complexity is linear as we iterate through each character once to populate both dictionaries and then count the special characters. 
    * Detailed explanation: The code iterates through the string only once, with two loops for the dictionary population, resulting in a time complexity of $O(N)$.

* **Space Complexity:** $O(1)$ - We are using dictionaries (`last_lower` and `first_upper`) to store character indices.  Dictionaries have constant space complexity.
    * Detailed explanation: We use dictionaries to store unique characters as keys, with their index values in the dictionary. This dictionary usage results in constant space complexity, making the overall space complexity of $O(1)$.