# Add Binary - Step by Step Approach

## Problem Statement
Given two binary strings `a` and `b`, return their sum as a binary string.

## Approach: Manual Binary Addition (Right to Left)

### Intuition
Just like adding decimal numbers by hand, we can add binary numbers from right to left, keeping track of the carry. Each position can have a sum of 0, 1, 2, or 3 (when including carry), and we compute the result digit and new carry accordingly.

### Step-by-Step Algorithm

1. **Initialize Pointers and Variables**
   - Set pointer `i` to the last index of string `a`
   - Set pointer `j` to the last index of string `b`
   - Initialize `carry = 0` to track overflow from each addition
   - Create an empty list `result` to store digits (efficient for appending)

2. **Iterate While There Are Digits or Carry**
   - Continue loop while `i >= 0` OR `j >= 0` OR `carry != 0`
   - This ensures we process all digits and any final carry

3. **Calculate Total for Current Position**
   - Start with `total = carry`
   - If `i >= 0`, add `int(a[i])` to total and decrement `i`
   - If `j >= 0`, add `int(b[j])` to total and decrement `j`

4. **Compute Result Digit and New Carry**
   - Append `str(total % 2)` to result (current binary digit)
   - Update `carry = total // 2` (carry for next position)

5. **Reverse and Join Result**
   - Since we built the result from right to left, reverse the list
   - Join all characters into a single string and return

### Example Walkthrough
```
Input: a = "1010", b = "1011"
Step-by-step addition (right to left):
Position 3: 0 + 1 + carry(0) = 1 → digit: 1, carry: 0
Position 2: 1 + 1 + carry(0) = 2 → digit: 0, carry: 1
Position 1: 0 + 0 + carry(1) = 1 → digit: 1, carry: 0
Position 0: 1 + 1 + carry(0) = 2 → digit: 0, carry: 1
Final carry: 1 → digit: 1
Result (reversed): "10101"
```

### Key Observations
- Binary addition rules: `0+0=0`, `0+1=1`, `1+1=10`, `1+1+1=11`
- Using a list for result is more efficient than string concatenation
- The loop condition `i >= 0 or j >= 0 or carry` handles strings of different lengths and final carry

## Complexity Analysis

### Time Complexity: O(max(m, n))
- Where `m` and `n` are the lengths of strings `a` and `b`
- We iterate through each digit of the longer string once
- Reversing the result list takes O(max(m, n)) time
- Overall: **O(max(m, n))**

### Space Complexity: O(max(m, n))
- The result list stores at most `max(m, n) + 1` characters (for potential final carry)
- No other significant extra space is used
- Overall: **O(max(m, n))**
