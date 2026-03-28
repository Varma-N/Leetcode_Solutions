# 3713. Longest Balanced Substring I

## Approach

To find the length of the longest balanced substring, we need to check various substrings of the given string and verify if they meet the "balanced" condition. A substring is considered balanced if every distinct character appearing in it occurs the same number of times.

### Step-by-Step Logic

1.  **Iterate Through All Substrings**
    Since the constraints allow for a quadratic solution, we can iterate through every possible starting index of the string. For each starting index, we extend the substring to every possible ending index. This ensures we consider all potential candidates for the longest balanced substring.

2.  **Track Character Frequencies**
    As we extend the substring from the start index to the current end index, we maintain a frequency count of each character encountered. Since the input consists only of lowercase English letters, a fixed-size array (or hash map) of size 26 is sufficient to store these counts efficiently.

3.  **Validate Balanced Condition**
    For each generated substring, we need to determine if it is balanced. To do this:
    *   Ignore characters that do not appear in the current substring (frequency is 0).
    *   Among the characters that do appear, find the minimum frequency and the maximum frequency.
    *   If the minimum frequency equals the maximum frequency, it implies all present characters have the same count. Therefore, the substring is balanced.

4.  **Update Maximum Length**
    We maintain a variable to track the maximum length found so far. Whenever we identify a valid balanced substring, we compare its length with the current maximum. If the new length is greater, we update the maximum. To optimize slightly, we can skip the validation step if the current substring length is not greater than the maximum length already found.

5.  **Return Result**
    After checking all possible substrings, the tracked maximum length represents the longest balanced substring. Note that a single character is always considered balanced, so the minimum possible answer is 1 (provided the string is not empty).

## Complexity Analysis

- **Time Complexity:** $O(N^2 \cdot 26)$
  - We use two nested loops to generate all substrings, which takes $O(N^2)$ where $N$ is the length of the string.
  - Inside the inner loop, we iterate over the frequency array of size 26 to check the balanced condition.
  - Since 26 is a constant, this simplifies to $O(N^2)$.

- **Space Complexity:** $O(1)$
  - We use a fixed-size frequency array of length 26 to store character counts.
  - This does not scale with the input size $N$, so it is considered constant space.
