from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total_sum = sum(sum(row) for row in grid)
        
        def check_horizontal(g: list[list[int]]) -> bool:
            m = len(g)
            n = len(g[0])
            if m < 2:
                return False
            
            top_counts = Counter()
            bot_counts = Counter(x for row in g for x in row)
            
            top_sum = 0
            bot_sum = total_sum
            
            for i in range(m - 1):
                for x in g[i]:
                    bot_counts[x] -= 1
                    top_counts[x] += 1
                
                row_sum = sum(g[i])
                top_sum += row_sum
                bot_sum -= row_sum
                
                if top_sum == bot_sum:
                    return True
                
                elif bot_sum > top_sum:
                    diff = bot_sum - top_sum
                    if bot_counts[diff] > 0:
                        bot_rows = m - 1 - i
                        if bot_rows > 1 and n > 1:
                            return True
                        elif n == 1:
                            if g[i + 1][0] == diff or g[m - 1][0] == diff:
                                return True
                        elif bot_rows == 1:
                            if g[i + 1][0] == diff or g[i + 1][n - 1] == diff:
                                return True
                                
                else:
                    diff = top_sum - bot_sum
                    if top_counts[diff] > 0:
                        top_rows = i + 1
                        if top_rows > 1 and n > 1:
                            return True
                        elif n == 1:
                            if g[0][0] == diff or g[i][0] == diff:
                                return True
                        elif top_rows == 1:
                            if g[0][0] == diff or g[0][n - 1] == diff:
                                return True
                                
            return False

        if check_horizontal(grid):
            return True
            
        transposed_grid = [list(col) for col in zip(*grid)]
        return check_horizontal(transposed_grid)
