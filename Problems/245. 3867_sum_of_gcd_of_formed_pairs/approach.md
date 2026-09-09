### Approach

The problem requires us to generate a new array of GCD values based on the running maximum of the input array, sort this new array, and then calculate the sum of the GCDs of specific pairs (smallest with largest). 

Here is the step-by-step execution of the logic:

1. **Initialize Tracking Variables:**
   * Create an empty list `prefixGcd` to store our generated GCD values.
   * Initialize a variable `current_max` to `0`. This will keep track of the maximum value seen so far as we iterate through the `nums` array.

2. **Construct the `prefixGcd` Array:**
   * Iterate through each number (`num`) in the `nums` array.
   * Update `current_max` by taking the maximum of `current_max` and `num`.
   * Calculate the Greatest Common Divisor (GCD) of the current `num` and `current_max` using `math.gcd()`.
   * Append this calculated GCD to the `prefixGcd` list.

3. **Sort the Array:**
   * Sort the `prefixGcd` list in non-decreasing order using the built-in `.sort()` method.

4. **Pair Elements and Sum their GCDs:**
   * Initialize a running total `ans` to `0`.
   * Determine the number of pairs by integer dividing the length of `prefixGcd` by 2 (`n // 2`). This inherently ignores the middle element if the length of the array is odd, exactly as the problem requires.
   * Loop `i` from `0` to `(n // 2) - 1`. 
   * In each iteration, pair the smallest available element `prefixGcd[i]` with the largest available element `prefixGcd[n - 1 - i]`.
   * Calculate the GCD of this pair and add it to `ans`.

5. **Return the Result:**
   * Finally, return the accumulated sum `ans`.

---

### Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n \log n + n \log M)$
  * Traversing the array to construct `prefixGcd` takes $\mathcal{O}(n \log M)$ time, where $n$ is the length of the array and $\log M$ represents the time taken to compute the GCD of two numbers (with $M$ being the maximum possible value in the array, up to $10^9$).
  * Sorting the `prefixGcd` array takes $\mathcal{O}(n \log n)$ time.
  * The final loop runs $n/2$ times, calculating the GCD of the pairs, which takes $\mathcal{O}(n \log M)$ time. 
  * Overall time complexity is dominated by the sorting and GCD operations: $\mathcal{O}(n \log n + n \log M)$.
* **Space Complexity:** $\mathcal{O}(n)$
  * The algorithm creates a new list `prefixGcd` of the same length as the input array `nums`, which takes $\mathcal{O}(n)$ auxiliary space. Sorting may also require up to $\mathcal{O}(n)$ space depending on the sorting algorithm implementation (like Timsort in Python).