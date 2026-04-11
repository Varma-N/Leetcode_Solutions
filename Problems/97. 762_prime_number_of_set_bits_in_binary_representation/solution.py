class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_set_bits = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(1 for i in range(left, right + 1) 
                  if bin(i).count('1') in prime_set_bits)
