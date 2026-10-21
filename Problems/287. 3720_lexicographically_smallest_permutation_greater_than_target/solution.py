class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        s_counts = collections.Counter(s)
        n = len(s)
        
        # Step 2 & 3: Iterate backwards to find the longest valid prefix match
        for i in range(n - 1, -1, -1):
            # Check what we need to form the prefix target[0...i-1]
            req_counts = collections.Counter(target[:i])
            
            # Verify if our pool has enough characters for this prefix
            possible = True
            for char, count in req_counts.items():
                if s_counts[char] < count:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # Calculate the remaining pool of letters after building the prefix
            rem_counts = s_counts.copy()
            for char, count in req_counts.items():
                rem_counts[char] -= count
                
            # Find the smallest available character strictly greater than target[i]
            best_char = None
            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)
                if char > target[i] and rem_counts[char] > 0:
                    best_char = char
                    break  # Found the smallest one, stop searching
            
            # Step 4: If we found a valid pivot character, build the final string
            if best_char:
                rem_counts[best_char] -= 1
                
                # Start with the matching prefix + our chosen strictly greater character
                result = target[:i] + best_char
                
                # Append the rest of the available characters in alphabetical order
                for char_code in range(ord('a'), ord('z') + 1):
                    char = chr(char_code)
                    result += char * rem_counts[char]
                    
                return result
                
        # Step 5: If no valid permutation is found
        return ""