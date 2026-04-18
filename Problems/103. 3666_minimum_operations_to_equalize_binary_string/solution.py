class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        c = s.count('0')
        
        # If there are no '0's, no operations are needed.
        if c == 0:
            return 0
        
        # If k == n, we must flip all bits in each operation.
        # If we have all '0's, 1 operation makes them all '1's.
        # If we have a mix, we oscillate and can never reach all '1's.
        if k == n:
            return 1 if c == n else -1
        
        # Parity check: x * k must have the same parity as c.
        # If k is even, x * k is even, so c must be even.
        if k % 2 == 0 and c % 2 != 0:
            return -1
        
        # Calculate lower bounds for x
        # 1. Total flips x * k must be at least c
        l1 = (c + k - 1) // k
        
        nk = n - k
        # 2. Capacity constraint if x is even: x >= c / (n - k)
        l2 = (c + nk - 1) // nk
        # 3. Capacity constraint if x is odd: x >= (n - c) / (n - k)
        l3 = (n - c + nk - 1) // nk
        
        if k % 2 != 0:
            # If k is odd, x must have the same parity as c
            required_parity = c % 2
            if required_parity == 0:
                # x must be even
                x = max(l1, l2)
                if x % 2 != 0:
                    x += 1
                return x
            else:
                # x must be odd
                x = max(l1, l3)
                if x % 2 == 0:
                    x += 1
                return x
        else:
            # If k is even, c is even. x can be even or odd.
            # Try even x
            x_even = max(l1, l2)
            if x_even % 2 != 0:
                x_even += 1
            
            # Try odd x
            x_odd = max(l1, l3)
            if x_odd % 2 == 0:
                x_odd += 1
            
            return min(x_even, x_odd)
