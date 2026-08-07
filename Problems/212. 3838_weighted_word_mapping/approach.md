# Problem 3838: Weighted Word Mapping

## Intuition
The problem requires mapping the weights of words to their corresponding letters in a specific order based on their weight modulo 26. This approach leverages character-frequency tables and efficient string manipulations to achieve this. The key is understanding how to map the weighted characters to their respective positions using reverse alphabetical order.

## Approach
1. **Initialization**:
   - Create a dictionary (`input_map`) mapping lowercase English characters (0-25) to their corresponding weights. 
     ```
     input_map = {chr(97+i): weights[i] for i in range(26)} 
     ```
   - Initialize an empty list `res` which will hold the mapped letters.

2. **Mapping**:
   - Iterate through each word: `for word in words:`
       -  Initialize `word_weight` to 0.
       -  Iterate through each character `char` in the current word: `for char in word:`
           -  Add the weight of `char` to `word_weight`.
       - Calculate `word_weight % 26` and append the corresponding character from the alphabet (`chr(122-word_weight)`) to the result list `res`.


3. **Result**:
   - Concatenate all characters in `res` into a string using `''.join(res)` and return it as the output string.



## Complexity Analysis

* **Time Complexity:** $O(N \cdot L)$ where N is the length of words, and L is the average length of each word
    - The algorithm iterates through the words and characters in a linear fashion with respect to the number of inputs.
* **Space Complexity:**  $O(1)$ 
    - The memory usage remains constant (in-place operation).
