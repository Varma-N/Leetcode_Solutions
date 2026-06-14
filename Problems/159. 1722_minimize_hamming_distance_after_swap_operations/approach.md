# Problem 1722: Minimize Hamming Distance After Swap Operations

## Approach

### Step-by-Step Breakdown
1. **Union Find**: The code utilizes a Union-Find data structure to efficiently group elements in the source array based on allowed swaps. It identifies connected components where swapping is possible.  
2. **Group Indices**: For each component, it lists all indices that belong to that group (connected by allowed swaps). 
3. **Count Matching Elements**: The code iterates through groups and counts how many elements from the source array are present in each group. 
4. **Calculate Hamming Distance**:  It calculates the Hamming distance between the source and target arrays after considering all possible swap operations.


## Complexity Analysis
* **Time Complexity:** $O(N \log N)$ (For union-find)
    * The time complexity is determined by the number of nodes in the Union-Find tree, which grows linearly with the input array size.  The merging and finding operations have a time complexity of $O(\log N)$. 
* **Space Complexity:** $O(N)$
    * The space complexity is dominated by the use of the Union-Find data structure for grouping indices and storing frequencies.  


=========================================