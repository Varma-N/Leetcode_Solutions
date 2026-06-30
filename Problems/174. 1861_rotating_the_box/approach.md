# Problem 1861: Rotating the Box

## Intuition
The core idea is to simulate a rotation of the box by considering the stones' final positions in relation to each other. We can perform this process iteratively, moving from one row down to the next and filling in empty slots based on the presence of obstacles or other stones. 


## Approach
1. **Initialization:**
    - Determine the number of rows (m) and columns (n) in the input matrix `boxGrid`.
2. **Iterative Rotation:**
    - Initialize `empty_slot` to the last column index (`cols - 1`).  This variable will track which column has an empty space.
    - Iterate through each column from right to left:
        - If a cell contains an '*' (obstacle), update `empty_slot` to the previous column by decrementing it.
        - If a cell contains '#' (stone), fill the cell with '.' and swap it with the corresponding empty slot from the same row (`empty_slot`).  Decrease `empty_slot` accordingly to find the next available space. 
3. **Building the Output Matrix:** 
    - Create a new matrix `res` with `rows x cols`.
    - Fill the `res` matrix by mapping each element of `boxGrid` to its corresponding position in `res` based on the rotation logic (this should be done iteratively).  


## Complexity Analysis

* **Time Complexity:** $O(m \cdot n)$ 
    * The time complexity is directly proportional to the size of the input matrix.  We iterate through each cell in `boxGrid`, and we perform a single swap operation for each stone that falls. 
* **Space Complexity:** $O(1)$ 
    * We use constant extra space to store the final output matrix.