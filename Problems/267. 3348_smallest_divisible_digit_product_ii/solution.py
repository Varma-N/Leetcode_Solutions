import sys
from math import gcd 
from functools import lru_cache

sys.set_int_max_str_digits(400000)
sys.setrecursionlimit(2000)

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
        if temp > 1:
            return "-1"
        
        factors = {
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }
        
        @lru_cache(None)
        def solve(a, b, c, d):
            if a == 0 and b == 0 and c == 0 and d == 0:
                return ""
            res = None
            for digit in range(2, 10):
                f = factors[digit]
                na = max(0, a - f[0])
                nb = max(0, b - f[1])
                nc = max(0, c - f[2])
                nd = max(0, d - f[3])
                
                if (na, nb, nc, nd) == (a, b, c, d):
                    continue
                    
                sub = solve(na, nb, nc, nd)
                if sub is not None:
                    cand = "".join(sorted(str(digit) + sub))
                    if res is None or len(cand) < len(res) or (len(cand) == len(res) and cand < res):
                        res = cand
            return res

        def get_req(val):
            req = [0, 0, 0, 0]
            for i, p in enumerate([2, 3, 5, 7]):
                while val % p == 0:
                    req[i] += 1
                    val //= p
            return req

        prefix_t = [t]
        for ch in num:
            if ch == '0':
                break
            prefix_t.append(prefix_t[-1] // gcd(prefix_t[-1], int(ch)))
        
        for i in range(len(prefix_t) - 1, -1, -1):
            if i == len(num):
                if prefix_t[i] == 1:
                    return num
                continue
            
            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                rem_t = prefix_t[i] // gcd(prefix_t[i], d)
                req = get_req(rem_t)
                sub = solve(*req)
                
                L = len(num) - 1 - i
                if len(sub) <= L:
                    return num[:i] + str(d) + '1' * (L - len(sub)) + sub
                
        req = get_req(t)
        sub = solve(*req)
        ans_len = max(len(num) + 1, len(sub))
        return '1' * (ans_len - len(sub)) + sub
