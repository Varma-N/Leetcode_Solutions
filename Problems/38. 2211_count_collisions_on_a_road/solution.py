class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove leading 'L's (cars moving left forever)
        left = 0
        while left < len(directions) and directions[left] == 'L':
            left += 1
        
        # Remove trailing 'R's (cars moving right forever)
        right = len(directions) - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        
        # No cars left that can collide
        if left > right:
            return 0
        
        # Count all moving cars in the middle section
        collisions = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1
        
        return collisions
