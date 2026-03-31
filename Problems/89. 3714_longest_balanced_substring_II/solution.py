class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        max_run = 1
        cur_run = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                cur_run += 1
                if cur_run > max_run:
                    max_run = cur_run
            else:
                cur_run = 1

        pa = pb = pc = 0
        diff_map = {(0, 0): 0}
        max_three = 0
        for i in range(1, n + 1):
            char = s[i - 1]
            if char == 'a':
                pa += 1
            elif char == 'b':
                pb += 1
            else:
                pc += 1
            d1 = pa - pb
            d2 = pa - pc
            key = (d1, d2)
            if key in diff_map:
                length = i - diff_map[key]
                if length > max_three:
                    max_three = length
            else:
                diff_map[key] = i

        max_two = 0
        pairs = [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')]
        for X, Y, Z in pairs:
            cur_sum = 0
            sum_map = {0: -1}
            for i in range(n):
                if s[i] == Z:
                    cur_sum = 0
                    sum_map = {0: i}
                    continue
                if s[i] == X:
                    cur_sum += 1
                else:
                    cur_sum -= 1
                if cur_sum in sum_map:
                    length = i - sum_map[cur_sum]
                    if length > max_two:
                        max_two = length
                else:
                    sum_map[cur_sum] = i

        return max(max_run, max_two, max_three)
        
