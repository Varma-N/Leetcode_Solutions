class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            shift = k % n

            if shift == 0:
                continue
            
            if i % 2 == 0:
                for j in range(n):
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
            else:
                for j in range(n):
                    if mat[i][j] != mat[i][(j - shift) % n]:
                        return False
        return True
