from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # Check if `s` can form a valid palindrome
        odd_chars = [char for char, count in cnt.items() if count % 2 != 0]
        if len(odd_chars) > (1 if n % 2 != 0 else 0):
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        avail_half = Counter({char: count // 2 for char, count in cnt.items()})
        k = n // 2
        
        # Condition A: The first half of the target perfectly matches our available half.
        if Counter(target[:k]) == avail_half:
            cand = target[:k] + mid_char + target[:k][::-1]
            if cand > target:
                return cand
                
        # Condition B: Find the smallest possible divergence that is greater than `target`
        max_match = 0
        rem_match = Counter(avail_half)
        for char in target[:k]:
            if rem_match[char] > 0:
                rem_match[char] -= 1
                max_match += 1
            else:
                break
                
        if k > 0:
            start_i = min(max_match, k - 1)
            
            # Setup initial remainders pool matching up to index `start_i`
            rem = Counter(avail_half)
            for j in range(start_i):
                rem[target[j]] -= 1
                
            # Iterate backward looking for the best breaking point
            for i in range(start_i, -1, -1):
                # Search for any remaining character strictly greater than target[i]
                valid_c = [char for char, count in rem.items() if count > 0 and char > target[i]]
                if valid_c:
                    best_c = min(valid_c)
                    rem[best_c] -= 1
                    
                    # Greedily construct the remainder with the smallest characters possible
                    rest = []
                    for char in sorted(rem.keys()):
                        if rem[char] > 0:
                            rest.extend([char] * rem[char])
                            
                    P = target[:i] + best_c + "".join(rest)
                    return P + mid_char + P[::-1]
                    
                # Backtrack: Add target[i-1] back into remainder pool for the next earlier break point evaluation
                if i > 0:
                    rem[target[i-1]] += 1
                    
        return "" 
