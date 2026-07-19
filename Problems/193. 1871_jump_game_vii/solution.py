class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        
        active_jumps = 0
        
        for i in range(1, n):
            if i >= minJump and reachable[i - minJump]:
                active_jumps += 1
            
            if i > maxJump and reachable[i - maxJump - 1]:
                active_jumps -= 1
            
            if active_jumps > 0 and s[i] == '0':
                reachable[i] = True
                
        return reachable[-1]
