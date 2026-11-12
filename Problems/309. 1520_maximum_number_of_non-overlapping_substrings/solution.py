class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: s.find(c) for c in set(s)}
        last = {c: s.rfind(c) for c in set(s)}
        
        intervals = []
        for c in set(s):
            l = first[c]
            r = last[c]
            i = l
            valid = True
            
            while i <= r:
                if first[s[i]] < l:
                    valid = False
                    break
                r = max(r, last[s[i]])
                i += 1
                
            if valid:
                intervals.append((r, l))
                
        intervals.sort()
        
        res = []
        last_end = -1
        
        for r, l in intervals:
            if l > last_end:
                res.append(s[l:r+1])
                last_end = r
                
        return res