class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x = y = 0
        di = 0 
        max_sq_dist = 0
        
        for cmd in commands:
            if cmd == -2: 
                di = (di + 3) % 4
            elif cmd == -1: 
                di = (di + 1) % 4
            else: 
                for _ in range(cmd):
                    nx, ny = x + dx[di], y + dy[di]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_sq_dist = max(max_sq_dist, x*x + y*y)
                    else:
                        break
                        
        return max_sq_dist
