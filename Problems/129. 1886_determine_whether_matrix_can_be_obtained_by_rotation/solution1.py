class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        def rotate90(matrix):
            n = len(matrix)
            new_matrix = [[0] * n for _ in range(n)]
            for i in range(0, n):
                for j in range(0, n):
                    new_matrix[j][n-1-i] = matrix[i][j]
            return new_matrix

        for _ in range(1, 4):
            mat = rotate90(mat)

            if mat == target:
                return True
        return False

        
        


        
