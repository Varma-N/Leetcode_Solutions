# Problem 3093: Longest Common Suffix Queries

## Intuition
The problem is about finding the longest common suffix of each string in `wordsQuery` within a given set of strings, `wordsContainer`. To achieve this efficiently, we leverage a Trie data structure and a systematic traversal strategy. 

## Approach
1. **Trie Construction:**
   - Create a Trie using `TrieNode` to represent prefixes.
   - For each string in `wordsContainer`, insert it into the Trie by traversing down the tree.  
   
2. **Query Processing:**
   - Start at the root node of the Trie (`root`).
   - Iterate through each query string `q`:
     - Traverse the Trie, checking if each character is present as a child of the current node. 
     - If the character is not found as a child (meaning there's no matching prefix), break the traversal; we stop here because we don't have a common suffix.  
     - If the character exists as a child, compare its `best_idx` to find the index of the string with the longest common suffix. 

## Complexity Analysis
* **Time Complexity:** $O(N)$ for building the Trie and $O(M)$ for processing queries, where N is the total number of strings in `wordsContainer`, M is the total number of strings in `wordsQuery`.  
    * The time complexity for constructing the Trie is linear to the length of each string. 
    * The time complexity for query processing remains linear as well, as we are traversing the Trie, checking if a character exists in its children.
* **Space Complexity:** $O(N)$
    * The space complexity represents the maximum number of nodes in the Trie.