# Minimum Distance to Type a Word Using Two Fingers - Approach

## Step-by-Step Approach

1. **Distance Calculation**: Establish a method to calculate the Manhattan distance between any two characters on a keyboard arranged in a grid with 6 columns. Treat the distance as 0 if a finger has not yet been placed on the keyboard.
2. **State Initialization**: Use dynamic programming to track the minimum typing effort required. Maintain a state mapping (like a hash map) where the key is the position of the "other" finger (the one not resting on the most recently typed character), and the value is the minimum accumulated distance. Initialize the state with one unplaced finger having a cost of 0.
3. **Character Iteration**: Traverse through the target word, examining adjacent pairs consisting of the current character and the immediately next character that needs to be typed.
4. **Evaluate Finger Moves (Transitions)**: For every known state (every known position of the "other" finger and its accumulated cost), evaluate two choices to press the next character:
    * **Option A (Move Active Finger)**: Keep the "other" finger where it is, and move the finger currently on the current character to the next character. The new cost is the previous cost plus the distance between the current character and the next character.
    * **Option B (Move Other Finger)**: Move the "other" finger from its current position to the next character. The finger that was on the current character now becomes the new "other" finger. The new cost is the previous cost plus the distance between the old "other" finger and the next character.
5. **Update State**: Store the minimum cost for each resulting position of the "other" finger in a temporary state map for the current iteration, minimizing the cost if multiple paths result in the same finger configurations. Once evaluated, replace the old state map with the new one.
6. **Determine Minimum Cost**: Once all characters in the word have been processed, the answer is simply the smallest value remaining in the state map.

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the length of the word. For each character transition, we iterate over the possible positions of the other finger. Since the keyboard only has 26 letters (plus 1 unplaced state), the inner loop runs at most 27 times, which is a constant $\mathcal{O}(1)$ operation. Thus, the overall time scales linearly with the length of the word.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The dynamic programming dictionary stores a maximum of 27 keys (representing the 26 possible letters and the initial unplaced state) at any given time, regardless of how long the input word is.
