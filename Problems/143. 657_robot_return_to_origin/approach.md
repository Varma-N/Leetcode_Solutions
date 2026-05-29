# Approach for Robot Return to Origin

## Step-by-Step Approach

1. **Understand the Coordinate System:** The robot starts at an origin point, which can be thought of as `(0, 0)` on a 2D grid.
2. **Isolate Axes:** Recognize that vertical movements ('U' and 'D') operate entirely independently of horizontal movements ('R' and 'L').
3. **Analyze Vertical Displacement:** For the robot to return to its original vertical position, every step taken Up ('U') must be exactly offset by a step taken Down ('D'). Therefore, the total count of 'U' moves must equal the total count of 'D' moves.
4. **Analyze Horizontal Displacement:** Similarly, for the robot to return to its original horizontal position, every step taken Right ('R') must be exactly offset by a step taken Left ('L'). Thus, the total count of 'R' moves must equal the total count of 'L' moves.
5. **Count Occurrences:** Traverse the given string of moves and count the exact occurrences of each of the four directional characters.
6. **Evaluate Conditions:** Check if both equality conditions hold true simultaneously:
   - Count of 'U' == Count of 'D'
   - Count of 'R' == Count of 'L'
7. **Return Result:** If both conditions are satisfied, the robot is back at the origin, so return true. Otherwise, return false.

## Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of the `moves` string. Counting the occurrences of each character requires iterating through the string. Although the string is scanned four separate times (once for each direction), this results in $O(4N)$ operations, which simplifies asymptotically to $O(N)$ time.
- **Space Complexity:** $O(1)$ auxiliary space. The algorithm only stores a few integer values for the counts of the characters, which requires a constant amount of extra memory regardless of the input string's length.
