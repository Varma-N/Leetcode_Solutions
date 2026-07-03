class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        for layer in range(num_layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            elements = []
            for j in range(left, right):
                elements.append(grid[top][j])
            for i in range(top, bottom):
                elements.append(grid[i][right])
            for j in range(right, left, -1):
                elements.append(grid[bottom][j])
            for i in range(bottom, top, -1):
                elements.append(grid[i][left])
            layer_size = len(elements)
            real_k = k % layer_size
            rotated = elements[real_k:] + elements[:real_k]
            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid
