# Fancy Sequence - Step-by-Step Approach

The problem asks us to maintain a sequence and perform append, addition-to-all, multiplication-to-all, and indexing operations. A naive update of all elements during every operation would be $O(N)$ per update, which is too slow.

## Core Logic: Linear Transformation

We treat the cumulative operations on the sequence as a single linear transformation:
$$f(x) = (mul \cdot x) + add \pmod{10^9 + 7}$$

### 1. State Initialization
* `values`: A list to store "normalized" versions of appended numbers.
* `mul`: A global multiplier (initially 1).
* `add`: A global increment (initially 0).
* `MOD`: $10^9 + 7$.

### 2. The `append(val)` Operation
When we add a new value, we want to store it such that when the *current* `mul` and `add` are applied later, the result is the original `val`. 
To do this, we "reverse" the current transformation:
1.  Subtract the current `add` from `val`.
2.  Divide by the current `mul` (using the modular multiplicative inverse).
3.  Store this normalized value in `values`.

### 3. The `addAll(inc)` Operation
This only affects the global `add` constant.
* `add = (add + inc) % MOD`

### 4. The `multAll(m)` Operation
This affects both the global multiplier and the existing increment.
* `mul = (mul * m) % MOD`
* `add = (add * m) % MOD`

### 5. The `getIndex(idx)` Operation
If the index is valid, we take the stored normalized value and apply the *current* global transformation:
* `return (values[idx] * mul + add) % MOD`

---

## Complexity Analysis

### Time Complexity
* **`append`**: $O(\log MOD)$ — The bottleneck is calculating the modular inverse using `pow(a, MOD - 2, MOD)`.
* **`addAll`**: $O(1)$ — Simple scalar addition.
* **`multAll`**: $O(1)$ — Simple scalar multiplication.
* **`getIndex`**: $O(1)$ — Single mathematical transformation.

### Space Complexity
* **$O(N)$** — Where $N$ is the number of elements appended to the sequence. We store each element exactly once in the `values` list.
