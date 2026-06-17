# Problem 2833: Furthest Point From Origin

## Intuition
The goal is to find the furthest point on a number line from the origin (0) after performing a series of 'L', 'R', and '_'. This can be achieved by considering the movement directions and their impact on the position.

## Approach
1. **Initialization:** Create a variable `dist` to store the distance from the origin, initialized to 0.
2. **Move Analysis:**  For each move in the `moves` string, analyze:
   - If 'L' or '_' is encountered: Move left by subtracting `i` from `dist`.
   - If 'R' or '_' is encountered: Move right by adding `i` to `dist`. 
3. **Distance Calculation:** Calculate the final distance (`dist`) at the end of all moves.


## Complexity Analysis
* **Time Complexity:** $O(N)$
    *  We iterate through the moves string once, resulting in linear time complexity.
* **Space Complexity:** $O(1)$ 
    * We use a constant amount of space regardless of input size.