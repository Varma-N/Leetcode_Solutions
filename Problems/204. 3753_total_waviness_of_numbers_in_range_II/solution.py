class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n_str: str) -> int:
            memo = {}
            def dfs(idx, is_tight, is_lz, prev1, prev2):
                if idx == len(n_str):
                    return 1, 0
                state = (idx, is_tight, is_lz, prev1, prev2)
                if state in memo:
                    return memo[state]
                
                limit = int(n_str[idx]) if is_tight else 9
                total_ways = 0
                total_wave = 0
                
                for curr in range(limit + 1):
                    nxt_tight = is_tight and (curr == limit)
                    
                    if is_lz:
                        if curr == 0:
                            ways, wave = dfs(idx + 1, nxt_tight, True, -1, -1)
                            total_ways += ways
                            total_wave += wave
                        else:
                            ways, wave = dfs(idx + 1, nxt_tight, False, curr, -1)
                            total_ways += ways
                            total_wave += wave
                    else:
                        contribution = 0
                        if prev2 != -1 and prev1 != -1:
                            if prev2 < prev1 and prev1 > curr:
                                contribution = 1
                            elif prev2 > prev1 and prev1 < curr:
                                contribution = 1
                        
                        ways, wave = dfs(idx + 1, nxt_tight, False, curr, prev1)
                        total_ways += ways
                        total_wave += wave + ways * contribution
                        
                memo[state] = total_ways, total_wave
                return memo[state]
            
            return dfs(0, True, True, -1, -1)[1]

        return solve(str(num2)) - solve(str(num1 - 1))