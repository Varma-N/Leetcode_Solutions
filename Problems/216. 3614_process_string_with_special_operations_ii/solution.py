class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        history = [0] * (n + 1)
        
        for i in range(n):
            c = s[i]
            curr = history[i]
            if c >= 'a':
                history[i+1] = curr + 1
            elif c == '*':
                history[i+1] = curr - 1 if curr > 0 else 0
            elif c == '#':
                history[i+1] = curr * 2
            else:
                history[i+1] = curr
                
        if k < 0 or k >= history[n]:
            return '.'
            
        for i in range(n - 1, -1, -1):
            c = s[i]
            prev = history[i]
            
            if c >= 'a':
                if k == prev:
                    return c
            elif c == '*':
                continue
            elif c == '#':
                if k >= prev:
                    k -= prev
            else:
                if prev > 0:
                    k = prev - 1 - k
                    
        return '.'
