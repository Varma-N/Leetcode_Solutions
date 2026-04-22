# Approach: Minimum Number of Deci-Binary Numbers

## 1. Problem Understanding
A **deci-binary** number is a positive integer that consists only of digits `0` and `1` (e.g., `101`, `11`, `1`). We are given a string `n` representing a large decimal integer, and we need to find the minimum number of deci-binary numbers required to sum up to `n`.

## 2. Key Insight (The "Aha!" Moment)
The core of this problem lies in looking at each digit position independently.

* Consider a single digit, for example, `7`.
* To get a `7` in a specific position using only `0`s and `1`s, you must have at least seven numbers that have a `1` in that position.
* If you have a digit `9`, you need at least nine numbers that have a `1` in that position.
* The digit that is the **largest** in the string `n` dictates the total number of deci-binary numbers needed. Because you can only contribute at most a `1` to any position per deci-binary number, the highest digit acts as the "bottleneck."

## 3. Step-by-Step Logic
To solve this efficiently, we don't actually need to perform any subtraction or complex partitioning. We only need to identify the "highest demand" digit.

1.  **Analyze the Input:** Treat the input string `n` as a collection of individual digits.
2.  **Scan for the Maximum:** Iterate through the string to find the largest character (digit) present.
3.  **Optimization (Early Exit):**
    * Since `9` is the highest possible digit in decimal, if we encounter a `'9'` anywhere in the string, we can immediately conclude the answer is `9`.
    * We can check for digits in descending order (`9`, then `8`, then `7`...) to find the maximum as quickly as possible.
4.  **Transformation:** Convert the character representing the maximum digit into an integer.
5.  **Return:** That integer is the minimum number of deci-binary numbers required.

## 4. Complexity Analysis

### Time Complexity: $O(L)$
* Where $L$ is the length of the string `n`.
* In the worst case (e.g., $n = "11112"$), we might scan the entire string.
* Even when using a loop from `'9'` down to `'1'`, each `in` check in Python can take $O(L)$, but since there are only a constant number of digits (9 total), it remains linear.

### Space Complexity: $O(1)$
* We are not using any additional data structures that scale with the input size. We only store a few variables for the iteration and comparison.
