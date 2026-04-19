class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        length = 0  # bit length of current number

        for i in range(1, n + 1):
            # Check if i is a power of 2 → bit length increases
            if (i & (i - 1)) == 0:
                length += 1
            
            # Shift result left by 'length' bits and add i
            result = ((result << length) + i) % MOD

        return result
            
