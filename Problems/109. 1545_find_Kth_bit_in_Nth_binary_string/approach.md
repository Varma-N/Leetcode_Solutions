# Step-by-Step Guide: Find Kth Bit in Nth Binary String

## Problem Understanding
The problem asks us to find the $k^{th}$ bit in a binary string $S_n$, which is generated based on the following rules:
1. $S_1 = "0"$
2. $S_n = S_{n-1} + "1" + reverse(invert(S_{n-1}))$ for $n > 1$

### Key Characteristics of $S_n$
- **Length**: The length of $S_n$ is $2^n - 1$.
- **Middle Bit**: The middle bit of $S_n$ is always `"1"`.
- **Symmetry with Inversion**: The second half of $S_n$ is the inverted and reversed version of the first half.

---

## Step-by-Step Logical Approach

### 1. Identify the Middle Point
For any string $S_n$, the middle index is located at $mid = 2^{n-1}$. 
- If $k$ is exactly at the $mid$ position, the bit is always `"1"`.

### 2. Determine the Half
Instead of constructing the string (which grows exponentially), we use a recursive-style logic to "zoom in" on $k$:
- **Left Half ($k < mid$)**: The bit at $k$ in $S_n$ is the same as the bit at $k$ in $S_{n-1}$. We can just move to $S_{n-1}$ and keep the same $k$.
- **Right Half ($k > mid$)**: The bit at $k$ in $S_n$ is part of the $reverse(invert(S_{n-1}))$ section. 
    - Because it is **reversed**, position $k$ in the second half corresponds to position $length - k + 1$ in the first half.
    - Because it is **inverted**, we must track how many times we have flipped the bit.

### 3. Track Inversions (Flip Count)
Every time we find that $k$ lies in the right half of the current string, we effectively transform the problem to finding a bit in the left half, but we acknowledge that the result will be **inverted**. 
- Keep a counter (`flip_count`) for every time you transition from the right half to the left half.

### 4. Base Case
Continue the process of reducing $n$ and updating $k$ until:
- You land exactly on a middle bit (`"1"`).
- You reach $S_1$, which is always `"0"`.

### 5. Final Output Determination
The result is determined by the starting bit (from the base case) and the total `flip_count`:
- If `flip_count` is even, the bit remains as found.
- If `flip_count` is odd, the bit is inverted.

---

## Complexity Analysis

### Time Complexity: $O(n)$
In each step of the algorithm, we reduce $n$ by 1. Since we perform a constant number of operations (comparisons and bit shifts) at each level of $n$, the total time complexity is proportional to $n$.

### Space Complexity: $O(1)$
The iterative approach uses only a few integer variables (`flip_count`, `mid`, `n`, `k`) to track the state. No additional data structures or recursive call stacks are used, leading to constant space complexity.
