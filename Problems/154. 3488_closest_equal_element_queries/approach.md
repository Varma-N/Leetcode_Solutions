# Problem 3488: Closest Equal Element Queries

## Approach

### Step-by-Step Breakdown

1.  **Map Indices by Value:** * Preprocess the `nums` array by creating a dictionary (`val_to_indices`) that maps each unique element value to a sorted list of all indices where that value appears.
2.  **Process Each Query:**
    * For a given query index `qi`, identify the `target_val` at `nums[qi]`. Retrieve the list of all indices where `target_val` occurs.
3.  **Check for Existence:** * If the target value appears only once (i.e., at `qi`), there is no other equal element to compare with. In this case, append `-1` to the results.
4.  **Find Nearby Indices:**
    * Use binary search (`bisect_left`) on the retrieved index list to locate the position of `qi`. 
    * Consider the immediate neighbors (the index before and the index after `qi`) as primary candidates for the closest equal element.
    * Additionally, include the first and last occurrences of the value in the list as candidates to handle edge cases in circular distance calculations.
5.  **Calculate Minimum Distance:** * For each candidate index, calculate the distance. Since the array is treated as circular, the distance between index $i$ and $j$ is $\min(|i - j|, N - |i - j|)$.
    * Keep track of and store the global minimum distance found among the candidates for that query.

## Complexity Analysis

* **Time Complexity:** $O(N + Q \log K)$
    * $N$ is the number of elements in the array, $Q$ is the number of queries, and $K$ is the maximum number of times a single value appears in `nums`. Preprocessing takes $O(N)$. For each query, binary search takes $O(\log K)$, and evaluating the constant number of candidates takes $O(1)$.
* **Space Complexity:** $O(N)$
    * We store every index of the array in the `val_to_indices` dictionary, which scales linearly with the input size.
