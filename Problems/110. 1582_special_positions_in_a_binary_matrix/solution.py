class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        col_sums = [sum(col) for col in zip(*mat)]
        return sum(1 for row in mat if row.count(1) == 1 and col_sums[row.index(1)] == 1)
