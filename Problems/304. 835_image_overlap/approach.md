```markdown
# Problem 835: Image Overlap

## Intuition
Given two binary images, `img1` and `img2`, we aim to find the largest possible overlap when translating `img1` across the grid, placing it on top of `img2`. The translation can move bits from the grid borders. We then count the number of matching positions (1s) in both images. Note that no rotation is applied.


## Approach
1. **Initialization:**
   - `n = len(img1)`: Determine the size of the images (number of rows and columns).

2. **Finding Overlapping Positions:**
   - Create two sets, `A` and `B`, to store coordinates of 1s in `img1` and `img2` respectively. 
   - Use sets to store coordinates of 1s in both images. 
   - **Iterate through coordinates:** 
      - For each coordinate (r, c) in `A` and `B`:
         - Calculate the difference between the coordinates: `(r2 - r1, c2 - c1)`. 
         - Use a counter `counts` to track the occurrences of these offsets. 
         - Increment the counter if the coordinates have a 1 in both images. 

3. **Determining the Overlap:** 
   - Determine the maximum count in `counts` using the `max()` function. 
   - Return the maximum count or 0 if `counts` is empty.


## Complexity Analysis
* **Time Complexity:** $O(N \cdot N)$ 
    * We iterate through the grid to count overlapping bits. 
* **Space Complexity:** $O(N)$ 
    * The `counts` variable is linear in the size of the images. 

```