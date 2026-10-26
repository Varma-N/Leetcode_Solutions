from collections import deque
from typing import List
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:     
        m, n = len(classroom), len(classroom[0])
        litter_pos = {}
        litter_id = 0
        start_r = start_c = -1
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_pos[(r, c)] = litter_id
                    litter_id += 1
                    
        if litter_id == 0:
            return 0
            
        target_mask = (1 << litter_id) - 1
        
        queue = deque([(start_r, start_c, energy, 0, 0)]) 
        visited = {(start_r, start_c, 0): energy}
        
        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()
            
            if curr_energy == 0:
                continue
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    next_mask = mask
                    
                    if classroom[nr][nc] == 'R':
                        next_energy = energy
                    elif classroom[nr][nc] == 'L':
                        next_mask |= (1 << litter_pos[(nr, nc)])
                        
                    if next_mask == target_mask and next_energy >= 0:
                        return moves + 1
                        
                    if next_energy >= 0 and next_energy > visited.get((nr, nc, next_mask), -1):
                        visited[(nr, nc, next_mask)] = next_energy
                        queue.append((nr, nc, next_energy, next_mask, moves + 1))
                        
        return -1