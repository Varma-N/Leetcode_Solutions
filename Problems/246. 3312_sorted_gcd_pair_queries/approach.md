### Approach

The problem requires us to find the GCD of all possible pairs without explicitly generating them, as doing so would exceed the time limits. Instead, we count the frequencies of each GCD using mathematical inclusion-exclusion, build a prefix sum of these counts, and use binary search to efficiently answer each query. 

Here is the step-by-step execution of the logic:

1. **Initialize Frequency Arrays:**
   * Find the maximum value in the `nums` array (`max_val`) to size our arrays appropriately.
   * Create a `count` array of size `max_val + 1` and iterate through `nums` to store the frequency of each number present in the input.

2. **Calculate Exact GCD Frequencies:**
   * Initialize an `exact` array of size `max_val + 1` to store the exact number of pairs that share a GCD of strictly `g`.
   * Iterate backwards from `max_val` down to `1` (let this be `g`).
   * For each potential GCD `g`, count how many numbers in the array are multiples of `g` by summing their frequencies.
   * Calculate the maximum possible pairs we can form from these multiples using the combinations formula: `multiples_count * (multiples_count - 1) // 2`.
   * The calculated pairs currently include pairs whose GCD is a strict multiple of `g` (e.g., `2g`, `3g`). To isolate the pairs with a GCD of exactly `g`, iterate through all multiples of `g` and subtract their `exact` pair counts.

3. **Construct the Cumulative Count Array:**
   * Create a `prefix` array to store the cumulative sum of our isolated `exact` counts.
   * Iterate from `1` to `max_val`, setting `prefix[i] = prefix[i - 1] + exact[i]`.
   * The value at `prefix[i]` now represents the total number of pairs whose GCD is less than or equal to `i`.

4. **Answer Queries using Binary Search:**
   * The query asks for the element at index `q` in a 0-indexed sorted conceptual array of all GCDs. This conceptually translates to finding the smallest GCD value whose cumulative pair count is strictly greater than `q`.
   * Use Python's built-in `bisect_right` on the `prefix` array for each query `q`. This performs a binary search to efficiently find and map the query index to the correct GCD value.
   * Return the list of these resolved GCD values.

---

### Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N + M \log M + Q \log M)$
  * Traversing the array to construct the initial `count` array takes $\mathcal{O}(N)$ time, where $N$ is the length of `nums`.
  * Calculating the `exact` counts involves a nested loop where the outer loop runs $M$ times (where $M$ is `max_val`) and the inner loop increments by multiples of `g`. The number of operations is bounded by the harmonic series $\frac{M}{1} + \frac{M}{2} + \frac{M}{3} + \dots + \frac{M}{M}$, which simplifies to $\mathcal{O}(M \log M)$ time.
  * Constructing the `prefix` array takes $\mathcal{O}(M)$ time.
  * For each of the $Q$ queries, performing a binary search (`bisect_right`) on the `prefix` array of size $M$ takes $\mathcal{O}(\log M)$ time, resulting in $\mathcal{O}(Q \log M)$ time for all queries.
  * Overall time complexity is dominated by the harmonic series traversal and the binary search operations.
* **Space Complexity:** $\mathcal{O}(M + Q)$
  * The algorithm creates auxiliary arrays `count`, `exact`, and `prefix`, all bounded by the maximum value in the input array, taking $\mathcal{O}(M)$ space.
  * Generating the final output array takes $\mathcal{O}(Q)$ space to store the answers for each query.