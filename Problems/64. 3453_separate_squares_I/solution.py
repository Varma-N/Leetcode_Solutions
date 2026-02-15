class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Step 1: Compute total area
        total_area = sum(l * l for _, y, l in squares)
        half_area = total_area / 2.0

        # Step 2: Binary search bounds
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        # Step 3: Helper function to compute area below a given y
        def area_below(y_line: float) -> float:
            area = 0.0
            for _, y, l in squares:
                if y_line <= y:
                    continue
                elif y_line >= y + l:
                    area += l * l
                else:
                    area += (y_line - y) * l
            return area

        # Step 4: Binary search for precise y-coordinate
        for _ in range(60):  # sufficient for high precision
            mid = (low + high) / 2
            if area_below(mid) < half_area:
                low = mid
            else:
                high = mid

        # Step 5: Return result
        return low
