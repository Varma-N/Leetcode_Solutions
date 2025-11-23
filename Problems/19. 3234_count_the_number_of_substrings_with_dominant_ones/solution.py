from typing import List
import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        Z_MAX = 200

        # Build list of all zero positions
        zero_pos = [-1]
        for i, c in enumerate(s):
            if c == '0':
                zero_pos.append(i)
        zero_pos.append(n)

        L = len(zero_pos)
        total = 0
        p = 1  # pointer for first zero >= current index i

        for i in range(n):
            # Move the pointer so that zero_pos[p] >= i
            while p < L and zero_pos[p] < i:
                p += 1

            # Case z = 0 : substring made only of 1's
            if p < L:
                end0 = zero_pos[p] - 1
            else:
                end0 = n - 1

            if end0 >= i:
                total += end0 - i + 1

            # Case z = 1..Z_MAX
            for z in range(1, Z_MAX + 1):
                if p + z - 1 >= L - 1:
                    break

                last_zero = zero_pos[p + z - 1]
                if last_zero >= n:
                    break

                # Minimum ending index to satisfy dominant condition
                min_end = max(last_zero, i + z + z * z - 1)

                # Maximum ending index is before next zero
                if p + z < L:
                    max_end = zero_pos[p + z] - 1
                else:
                    max_end = n - 1

                if min_end <= max_end:
                    total += max_end - min_end + 1

        return total
