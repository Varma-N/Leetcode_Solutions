class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        for row in grid:
            count = 0
            for k in range(n - 1, -1, -1):
                if row[k] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
        
        swaps = 0
        for i in range(n):
            needed = n - 1 - i
            j = i
            while j < n and zeros[j] < needed:
                j += 1
            if j == n:
                return -1
            val = zeros.pop(j)
            zeros.insert(i, val)

            swaps += (j - i)
            
        return swaps
