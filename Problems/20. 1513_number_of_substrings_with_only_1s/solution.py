class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        count = 0  # current streak of consecutive '1's

        for char in s:
            if char == '1':
                count += 1
            else:
                total = (total + count * (count + 1) // 2) % MOD
                count = 0

        # Add final streak if string ends with '1'
        total = (total + count * (count + 1) // 2) % MOD

        return total
