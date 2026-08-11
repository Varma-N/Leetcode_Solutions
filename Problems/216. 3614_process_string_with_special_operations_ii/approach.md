# Problem 3614: Process String with Special Operations II

## Intuition
Given a string `s` and an array of operations, we need to find the result of applying these operations on the string. Each operation consists of performing two types:  either a single replacement or a series of replacements that are applied as follows: 
   * Replace every occurrence of a letter in the alphabet with its numerical representation (A=1, B=2, ..., Z=26). 

For example, if the string `s = "leet"` and the operation is "replace l with L," then "leet" would become "Leet."


## Approach
1. **Data Structures:**
   -  We will use a String (`str`) to store the input string `s`.
   -  We will use a vector of characters (`char_arr`) to represent our special operations. 

2. **Initialization:**
   -  `char_arr`: This array stores all possible operations, where each element is a character that represents an operation in the code. For example, if we have 's = "leet" and `char_arr` is `['l', 'e', 't']`, then 'replace l with L' would occur on this string and will result in `"Leet"`. 

3. **Looping through Operations:**
   -  For each operation in the `char_arr` vector, perform the following:
     -  Replace all occurrences of a given letter in the alphabet with its numerical representation (`A=1`, ... , `Z=26`). This can be achieved using ASCII mapping. 

4. **Result:**
   -  The modified string after applying the operations to the original input string `s` will give us the final result.



## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the length of the string. This is due to the single replacement operation taking constant time per character in the alphabet (`A=1`, ... , `Z=26`). 

    * The number of operations we perform will be directly related to the size of the input string `s`. If the string has N characters, each operation will have a complexity of O(N).

* **Space Complexity:** $O(1)$
    *  We are only storing a small set of variables in our code and they have constant space requirements.