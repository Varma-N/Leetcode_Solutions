from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for n in nums:
            divisors = set()
            # Only iterate up to sqrt(n)
            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    # Early exit if more than 4 divisors
                    if len(divisors) > 4:
                        break
            if len(divisors) == 4:
                total += sum(divisors)
                
        return total
        
