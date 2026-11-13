# Problem 1401: Circle and Rectangle Overlapping

## Intuition
The solution leverages the properties of circles and rectangles to determine if they overlap.  By considering the closest points on the boundaries of the rectangle, we can check if the circle touches the rectangle or if their boundaries intersect. 


## Approach
1. **Find the Closest Point:** Determine the closest point on the rectangle's boundary to the circle's center. This point lies on the line segment connecting the circle's center to the rectangle's edges. We use the following formula to find the closest x and y coordinates for the circle's center and the rectangle's boundary.  
    * `closest_x = max(x1, min(xCenter, x2))`
    * `closest_y = max(y1, min(yCenter, y2))` 
2. **Calculate Distance:**  Calculate the squared distance between the circle's center and the `closest_x` and `closest_y` coordinates. This involves the following formula:
    * `distance_x = xCenter - closest_x` 
    * `distance_y = yCenter - closest_y` 
3. **Check Overlap:** Using the calculated distances, determine if the squared distance between the circle's center and the closest point on the rectangle's boundary is less than or equal to the circle's radius. This condition signifies an overlap.
   
   

## Complexity Analysis
* **Time Complexity:** $O(1)$ 
    *  The algorithm only involves constant-time operations (finding the closest points and calculating the distances)
* **Space Complexity:** $O(1)$
    * The algorithm only uses constant-sized data structures, such as `closest_x`, `closest_y`, and `distance_x`, `distance_y`.