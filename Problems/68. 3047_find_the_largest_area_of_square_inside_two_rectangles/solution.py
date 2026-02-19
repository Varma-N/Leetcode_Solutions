class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        
        # Try every pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                
                # Rectangle i
                x1, y1 = bottomLeft[i]
                x2, y2 = topRight[i]
                
                # Rectangle j
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]
                
                # Intersection coordinates
                left = max(x1, x3)
                right = min(x2, x4)
                bottom = max(y1, y3)
                top = min(y2, y4)
                
                # Check if they overlap
                if right > left and top > bottom:
                    width = right - left
                    height = top - bottom
                    
                    # Largest square inside the intersection
                    side = min(width, height)
                    max_area = max(max_area, side * side)
        
        return max_area
