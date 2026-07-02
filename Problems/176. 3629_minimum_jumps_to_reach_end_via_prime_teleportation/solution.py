from collections import deque
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x > 1 and spf[x] == x

        prime_to_indices = {}
        for i, val in enumerate(nums):
            temp = val
            factors = set()
            d = temp
            while d > 1:
                p = spf[d]
                factors.add(p)
                while d % p == 0:
                    d //= p
            
            for p in factors:
                if p not in prime_to_indices:
                    prime_to_indices[p] = []
                prime_to_indices[p].append(i)

        queue = deque([(0, 0)])
        visited_indices = {0}
        visited_primes = set()

        while queue:
            idx, dist = queue.popleft()
            
            if idx == n - 1:
                return dist
            
            for neighbor in [idx - 1, idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))
            
            p = nums[idx]
            if is_prime(p) and p not in visited_primes:
                visited_primes.add(p)
                if p in prime_to_indices:
                    for neighbor in prime_to_indices[p]:
                        if neighbor not in visited_indices:
                            visited_indices.add(neighbor)
                            queue.append((neighbor, dist + 1))
                            
        return -1
            