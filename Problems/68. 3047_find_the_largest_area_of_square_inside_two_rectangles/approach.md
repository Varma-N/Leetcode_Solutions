# Approach: Largest Area of Square Inside Two Rectangles

## Problem Overview
Given a set of $N$ axis-aligned rectangles defined by their bottom-left and top-right coordinates, the goal is to find the maximum area of a square that can fit inside the intersection of **any two** distinct rectangles.

## Intuition
A square can only exist inside the overlapping region (intersection) of two rectangles. If two rectangles do not overlap, no valid square can be formed between them. If they do overlap, their intersection forms a new rectangular region. The largest square that can fit inside this intersection rectangle is determined by the shorter side of the intersection (either width or height).

To find the global maximum, we must evaluate every possible pair of rectangles, calculate their intersection, determine the largest valid square for that pair, and track the maximum area found across all pairs.

## Step-by-Step Algorithm

1.  **Initialize Maximum Area**: Start with a variable `max_area` set to 0. This will store the largest square area found so far.

2.  **Iterate Through All Pairs**: Use a nested loop structure to compare every unique pair of rectangles $(i, j)$ where $i < j$. This ensures each pair is checked exactly once without redundancy.

3.  **Extract Coordinates**: For each rectangle in the pair, retrieve the bottom-left $(x_1, y_1)$ and top-right $(x_2, y_2)$ coordinates.

4.  **Calculate Intersection Boundaries**: Determine the coordinates of the overlapping rectangle using the following logic:
    *   **Left Boundary**: The maximum of the two left x-coordinates.
    *   **Right Boundary**: The minimum of the two right x-coordinates.
    *   **Bottom Boundary**: The maximum of the two bottom y-coordinates.
    *   **Top Boundary**: The minimum of the two top y-coordinates.

5.  **Validate Overlap**: Check if a valid intersection exists. An intersection is valid only if:
    *   The `Right Boundary` is strictly greater than the `Left Boundary`.
    *   The `Top Boundary` is strictly greater than the `Bottom Boundary`.
    *   If either condition fails, the rectangles do not overlap, and we skip to the next pair.

6.  **Calculate Dimensions**: Compute the width and height of the intersection rectangle:
    *   `width = Right Boundary - Left Boundary`
    *   `height = Top Boundary - Bottom Boundary`

7.  **Determine Largest Square**: The side length of the largest square that fits inside this intersection is the minimum of the width and height (`side = min(width, height)`).

8.  **Update Maximum**: Calculate the area (`side * side`) and update `max_area` if this value is larger than the current maximum.

9.  **Return Result**: After checking all pairs, return `max_area`.

## Complexity Analysis

### Time Complexity
$$O(N^2)$$
We use a nested loop to iterate through all unique pairs of rectangles. If there are $N$ rectangles, the number of pairs is $\frac{N \times (N-1)}{2}$, which simplifies to $O(N^2)$. Inside the loop, all operations (coordinate extraction, comparison, arithmetic) are constant time $O(1)$.

### Space Complexity
$$O(1)$$
The algorithm uses a fixed number of variables to store coordinates, dimensions, and the maximum area. The space required does not grow with the input size $N$.
