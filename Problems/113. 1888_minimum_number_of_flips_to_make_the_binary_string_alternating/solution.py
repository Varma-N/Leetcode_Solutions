class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s

        mismatches = [0] * (2*n)
        for i in range(2*n):
            expected = '0' if i % 2 == 0 else '1'
            if s2[i] != expected:
                mismatches[i] = 1
        current_diff = sum(mismatches[:n])

        min_ops = min(current_diff, n - current_diff)

        for i in range(1, n):
            current_diff -= mismatches[i - 1]
            current_diff += mismatches[i + n - 1]
            min_ops = min(min_ops, min(current_diff, n - current_diff))
        return min_ops
