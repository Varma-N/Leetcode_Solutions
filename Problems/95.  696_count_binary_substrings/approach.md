# 696. Count Binary Substrings - Approach & Intuition

## Problem Understanding
The goal is to count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

For example:
- `0011` contains `01` and `0011`.
- `10101` contains `10`, `01`, `10`, `01`.

## Step-by-Step Intuition

### 1. Identify Consecutive Groups
Instead of checking every possible substring (which is O(N^2)), we can look at the string as a sequence of groups of consecutive identical characters.
- Example: `0011100` becomes groups of sizes `[2, 3, 2]` (two 0's, three 1's, two 0's).

### 2. Compare Adjacent Groups
A valid substring can only be formed between two adjacent groups of different characters (a group of 0's next to a group of 1's, or vice versa). 
- If we have `00` (size 2) and `111` (size 3), we can form:
  - `01`
  - `0011`
- We cannot form `000111` because there are only two 0's available. 
- Therefore, the number of valid substrings that can be formed between two adjacent groups is the **minimum** of the counts of those two groups.

### 3. One-Pass Optimization
We can calculate the result in a single pass without storing the entire list of group sizes:
- **`prev`**: Stores the length of the previous group of identical characters.
- **`curr`**: Stores the length of the current group of identical characters.
- Iterate through the string starting from the second character:
    - If the current character is the same as the previous one, increment `curr`.
    - If the current character is different, the previous group has ended. Set `prev` to the value of `curr`, and reset `curr` to 1.
- After every character check (or group transition), if `prev >= curr`, it means the current group can "match" with a part of the previous group to form a valid substring. Increment the total count by 1.

### 4. Why `prev >= curr` works?
As `curr` grows, every time it is less than or equal to `prev`, we have found one new valid substring. 
- Example `00011`:
  - At first `1`: `prev=3, curr=1`. (Found `01`)
  - At second `1`: `prev=3, curr=2`. (Found `0011`)
  - Total found: 2.

## Complexity Analysis

### Time Complexity
- **$O(N)$**: We traverse the string exactly once, where $N$ is the length of the string. Each operation inside the loop (comparison and addition) is $O(1)$.

### Space Complexity
- **$O(1)$**: We only use a constant amount of extra space to store the variables `prev`, `curr`, and `res`, regardless of the size of the input string.
