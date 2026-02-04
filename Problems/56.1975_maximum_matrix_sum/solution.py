class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_abs = 0
        min_abs = float('inf')
        neg_count = 0
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                    val = -val  
                
                sum_abs += val
                if val < min_abs:
                    min_abs = val
        
        if neg_count & 1:  
            return sum_abs - (min_abs << 1)  
        else:
            return sum_abs
