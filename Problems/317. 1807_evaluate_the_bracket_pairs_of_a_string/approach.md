# Problem 1807: Evaluate the Bracket Pairs of a String

## Intuition
To evaluate the bracket pairs of a string, we need to iterate through the string and, when encountering an opening bracket,  identify and replace the corresponding value with the knowledge array. 

## Approach
1. **Initialization:**
   - `knowledge_dict`: Create a dictionary to map keys from the `knowledge` array to their corresponding values. 
   - `result`: Initialize an empty list to store the final string after evaluating all brackets.
   - `current_key`: Initialize an empty string to track the current key being evaluated.
   - `inside_bracket`: Flag to track whether we're inside a bracket pair (initially false).

2. **Iterating through the string:**
   - Loop through each character in the string `s`.
   - **Opening Bracket:**
     - If the character is an opening bracket `(`:
       - Set `inside_bracket` to `True`.
   - **Closing Bracket:** 
     - If the character is a closing bracket `)`:
       - Set `inside_bracket` to `False`. 
       - Append the corresponding value from `knowledge_dict` (if it exists) to `result`.
       -  Reset `current_key`.
   - **In-Bracket Character:**
     - If inside a bracket pair, append the current character (`s[i]`) to `current_key`.
   - **Non-Bracket Character:**
     - If not inside a bracket pair, append the current character to `result`.

3. **Joining the result:**
   - Concatenate all elements in `result` into a single string and return it.

## Complexity Analysis
* **Time Complexity:** $O(N)$ where `N` is the length of the input string `s`. 
    * We iterate through the string once to process each character.
* **Space Complexity:** $O(1)$ 
    *  The algorithm only utilizes a constant amount of extra space for variables and a dictionary.