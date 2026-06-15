```markdown
# Problem 2452: Words Within Two Edits of Dictionary

## Intuition
The problem asks for words in the `queries` array that can be transformed into a word in the `dictionary` array with a maximum of two edits. A "two-edit" condition is to swap or insert characters, but not change whole letters within each word. This solution leverages a simple and efficient approach using a pre-processing step where we compare words from `queries` and `dictionary`.

## Approach
1. **Initialization:** 
   *  Create an empty list `result`, which will store the matching words.
2. **Iteration:**
   * Iterate through each query in the `queries` array:
     * For each query, call the `get_dis` function (detailed below) to compare it with each word in the `dictionary`. 
3. **Matching and Resulting List:** 
    * If a match is found (`get_dis` returns `True`), append the matching query to the `result` list.  
4. **Return:** Return the `result` array containing the words from the queries that match with some word in the dictionary after a maximum of two edits.

**Function Breakdown: get_dis(s1, s2)** 
This function checks if two strings `s1` and `s2` are "equivalent" given a specific edit rule (two edits).  
* **Initialization:**
    *  Create a variable `diff` to count the number of character swaps/insertions, initialized to 0.
* **Comparison Loop:**
    * Iterate through each character pair in `s1` and `s2` using `zip(s1, s2)` (allows for easy comparison).
    * If a character at position `q` in `s1` does not match the corresponding character `d` in `s2`, increment `diff`. 
    * If the `diff` value exceeds 2 after processing all characters, return `False` as we've exceeded the allowed edits.  
    * If no mismatches are found and the loop completes, return `True`, signifying equivalent strings.


## Complexity Analysis

* **Time Complexity:** $O(N \cdot M)$ where N is the number of words in the `queries` array, and M is the number of words in the `dictionary`. 
    * This complexity arises from iterating through both arrays for each word and comparing them using nested loops.  
* **Space Complexity:** $O(1)$.
    * The time complexity has a dominant factor which is the number of characters we need to compare. We are only dealing with basic string operations (comparing, swapping, or inserting characters), so our space complexity remains constant regardless of the length of the strings in our input data.  

``` 
INPUT DATA TO ANALYZE 
(DO NOT PRINT THIS) : Problem Context: You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length. In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary. 
Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

Example 1: 

Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation: 
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood". 
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke". 
- It would take more than 2 edits for "ants" to equal a dictionary word. 
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word. 
Thus, we return ["word","note","wood"].

Example 2: 

Input: queries = ["yes"], dictionary = ["not"] 
Output: [] 
Explanation:  Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.



Constraints: 

1 <= queries.length, dictionary.length <= 100
n == queries[i].length == dictionary[j].length
1 <= n <= 100 
All queries[i] and dictionary[j] are composed of lowercase English letters. 
 
```



 
```python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def get_dis(s1, s2):
            diff = 0
            for q, d in zip(s1, s2):
                if q != d:
                    diff += 1
                if diff > 2:
                    return False
            return True

        result = []
        for query in queries:
            for word in dictionary:
                if get_dis(query, word):  
                    result.append(query)
                    break
        return result
```