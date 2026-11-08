# Problem 836: Rectangle Overlap

## Intuition
Two rectangles overlap if and only if they share a common area.  We can determine this by checking if their bottom-left and top-right corners have a valid intersection, i.e., are within the boundary of one another.  This can be determined by a simple comparison of the coordinates.

## Approach
1.  **Input Validation:** Ensure that the input is valid - i.e., the input is in the format of a list of four integers for each rectangle, representing the bottom-left and top-right coordinates of the rectangle.  
2.  **Rectangle Boundaries:** Determine the boundaries of each rectangle.  This is done by comparing the coordinates of the bottom-left and top-right corners of each rectangle.
3.  **Overlap Check:**  If the boundaries of the rectangles overlap, return `True` as a boolean value, indicating that the rectangles overlap.  If the boundaries do not overlap, return `False`.

## Complexity Analysis
* **Time Complexity:**  $O(1)$
    * The algorithm performs a constant number of comparisons, making the time complexity independent of the input size. 
* **Space Complexity:** $O(1)$
    * The algorithm requires a constant amount of additional space, regardless of the input size.