class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            for j in range(n):
                if row[j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            sorted_heights = sorted(heights, reverse = True)

            for k, h in enumerate(sorted_heights):
                current_area = h * (k + 1)
                max_area = max(max_area, current_area)
        return max_area    
