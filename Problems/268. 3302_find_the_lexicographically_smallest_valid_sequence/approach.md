# Problem 3302: Find the Lexicographically Smallest Valid Sequence

## Intuition
The algorithm leverages suffix arrays to efficiently determine valid sequences. It precomputes the lengths of suffixes that match, enabling us to greedily pick indices that minimize the number of changes required.

## Approach
1. **Suffix Array Precomputation:** The `suf` array is precomputed to store the lengths of suffixes of `word1` that match `word2` starting from index `0`. This precomputation is crucial for efficiency.

2. **Greedy Index Selection:**  The algorithm iterates through `word2`. For each character position `k`, it attempts to match it with `word1` starting at index `i`. 
   - If the character matches, it increments `i` if `changed` is true (if the previous character change is not used)
   - If the character doesn't match, it checks if we can make a change to the sequence. 

3. **Lexicographically Smallest Sequence:**  The algorithm maintains a `seq` list to store the lexicographically smallest sequence of indices. If the sequence length is equal to `word2.length`, we return the `seq` list. If not, we return an empty list.


## Complexity Analysis
* **Time Complexity:** $O(N \log N)$  
    * Precomputation of the suffix array takes $O(N \log N)$ time.
* **Space Complexity:** $O(N)$  
    * The `suf` array stores the lengths of suffixes and requires $O(N)$ space.
