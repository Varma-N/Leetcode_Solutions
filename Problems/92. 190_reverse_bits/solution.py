class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)  # Add last bit of n to result
            n >>= 1                           # Shift n right
        return result
