# Problem 3783: Mirror Distance of an Integer

## Approach

### Step-by-Step Breakdown

1.  **Define a Helper Function (`rev`):**
    * Create a function to compute the reverse of an integer. 
    * Initialize `r` (the reversed number) to 0. 
    * While the input `num` is greater than 0, extract the last digit using the modulo operator (`num % 10`), add it to `r` after shifting `r`'s digits to the left (`r * 10`), and remove the last digit from `num` using integer division (`num // 10`).
2.  **Calculate the Mirror:**
    * Call the `rev` function on the input integer `n` to obtain its "mirror" image.
3.  **Determine Absolute Distance:**
    * Subtract the reversed number from the original number `n`.
    * Return the absolute value of this difference (`abs(n - rev(n))`) to get the total distance between the integer and its mirrored counterpart.

## Complexity Analysis

* **Time Complexity:** $O(D)$
    * Where $D$ is the number of digits in the integer $n$. Reversing an integer requires iterating through each of its digits exactly once, performing constant time mathematical operations at each step. Since $D = \log_{10}(n)$, the complexity can be expressed as $O(\log n)$.
* **Space Complexity:** $O(1)$
    * The algorithm uses a fixed amount of extra space to store the reversed number and the loop variables, regardless of the size of the input integer.
