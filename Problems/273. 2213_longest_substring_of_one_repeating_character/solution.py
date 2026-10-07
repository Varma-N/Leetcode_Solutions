class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        N = 1
        while N < n:
            N *= 2
            
        sz = [0] * (2 * N)
        pc = [''] * (2 * N)
        pl = [0] * (2 * N)
        sc = [''] * (2 * N)
        sl = [0] * (2 * N)
        ml = [0] * (2 * N)
        
        for i in range(n):
            idx = N + i
            sz[idx] = 1
            pc[idx] = s[i]
            pl[idx] = 1
            sc[idx] = s[i]
            sl[idx] = 1
            ml[idx] = 1
            
        for i in range(n, N):
            idx = N + i
            sz[idx] = 1
            
        for i in range(N - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            sz[i] = sz[left] + sz[right]
            pc[i] = pc[left]
            pl[i] = pl[left]
            if pl[left] == sz[left] and sc[left] == pc[right] and sc[left] != '':
                pl[i] += pl[right]
            sc[i] = sc[right]
            sl[i] = sl[right]
            if sl[right] == sz[right] and pc[right] == sc[left] and pc[right] != '':
                sl[i] += sl[left]
            ml[i] = ml[left] if ml[left] > ml[right] else ml[right]
            if sc[left] == pc[right] and sc[left] != '':
                cand = sl[left] + pl[right]
                if cand > ml[i]:
                    ml[i] = cand
                    
        ans = []
        for q_idx, q_char in zip(queryIndices, queryCharacters):
            idx = N + q_idx
            pc[idx] = q_char
            sc[idx] = q_char
            
            idx //= 2
            while idx > 0:
                left = 2 * idx
                right = 2 * idx + 1
                pc[idx] = pc[left]
                pl[idx] = pl[left]
                if pl[left] == sz[left] and sc[left] == pc[right] and sc[left] != '':
                    pl[idx] += pl[right]
                sc[idx] = sc[right]
                sl[idx] = sl[right]
                if sl[right] == sz[right] and pc[right] == sc[left] and pc[right] != '':
                    sl[idx] += sl[left]
                ml[idx] = ml[left] if ml[left] > ml[right] else ml[right]
                if sc[left] == pc[right] and sc[left] != '':
                    cand = sl[left] + pl[right]
                    if cand > ml[idx]:
                        ml[idx] = cand
                idx //= 2
            ans.append(ml[1])
            
        return ans