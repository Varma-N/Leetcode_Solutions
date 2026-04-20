# Step-by-Step Approach: Minimum Operations to Equalize Binary String

### 1. Initial Scanning and Base Case
* **Count Zeros:** Calculate the total number of '0's in the string (c).
* **Zero Operations:** If c = 0, the string is already all '1's. Return 0.

### 2. Boundary and Edge Cases
* **Window Size Constraint:** If k = n (the flip size equals string length):
    * If the string is all '0's (c = n), it takes exactly 1 operation.
    * If the string is a mix of '0's and '1's, it is impossible to equalize because flipping toggles everything simultaneously. Return -1.

### 3. Parity Validation
* **Even k Constraint:** If the window size k is even, every operation flips an even number of bits. 
    * Consequently, the count of zeros (c) must be even to be reachable.
    * If k is even and c is odd, return -1.

### 4. Mathematical Lower Bounds
To find the minimum number of operations (x), we define three lower bounds based on the physical limits of the string:
* **Coverage Bound (L1):** x must be large enough so that x * k flips can cover at least c zeros. 
    * L1 = ceil(c / k)
* **Even-Operation Capacity (L2):** When x is even, the maximum number of zeros we can effectively flip to '1' without forcing '1's to '0' is limited by the remaining space (n - k).
    * L2 = ceil(c / (n - k))
* **Odd-Operation Capacity (L3):** When x is odd, the constraint shifts to ensuring the initial '1's end up as '1's.
    * L3 = ceil((n - c) / (n - k))

### 5. Parity-Based Optimal x Selection
* **Case A: k is Odd**
    * The parity of x must match the parity of c.
    * If c is even: x = max(L1, L2). If result is odd, add 1.
    * If c is odd: x = max(L1, L3). If result is even, add 1.
* **Case B: k is Even**
    * x can be even or odd (since c is guaranteed to be even from step 3).
    * Calculate potential even x from max(L1, L2).
    * Calculate potential odd x from max(L1, L3).
    * Return the minimum of the two.

---

### Complexity Analysis
* **Time Complexity:** O(N) - Requires one pass to count the characters in the string. All subsequent mathematical calculations are O(1).
* **Space Complexity:** O(1) - Only a constant amount of extra space is used for variables, regardless of string size.
