class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1. Calculate how many codes we need (2^k)
        needed = 1 << k
        
        # 2. Quick math check (optimization)
        if len(s) < needed :
            return False
            
        # 3. Initialize the set
        seen = set()

        # 4. Loop through the string
        # Hint: range should stop at len(s) - k + 1
        for i in range(len(s) - k + 1):
            # Extract substring
            sub = s[i: i+k]
            
            # Add to set
            seen.add(sub)
            
            # Check if we found them all yet
            if len(seen) == needed:
                return True
                
        # 5. If loop finishes without returning True
        return False
