class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        # 1. Basic Validation of the LCP Matrix structure
        for i in range(n):
            for j in range(n):
                # Symmetry check
                if lcp[i][j] != lcp[j][i]:
                    return ""
                # Diagonal check: lcp[i][i] must be the length of the suffix starting at i
                if lcp[i][i] != n - i:
                    return ""
                # Value range check
                if lcp[i][j] > n - max(i, j):
                    return ""
                
                # Consistency check: If lcp[i][j] > 0, it must be 1 + lcp[i+1][j+1]
                # We handle boundary where i+1 or j+1 is out of bounds
                if lcp[i][j] > 0:
                    expected_next = 0
                    if i + 1 < n and j + 1 < n:
                        expected_next = lcp[i+1][j+1]
                    if lcp[i][j] != expected_next + 1:
                        return ""

        # 2. Construct the String Greedily
        # chars[i] stores the integer representation of the character at index i (0='a', 1='b', ...)
        chars = [-1] * n
        current_char_code = 0
        
        for i in range(n):
            if chars[i] != -1:
                continue
            
            # If we need more than 26 characters, it's impossible
            if current_char_code >= 26:
                return ""
            
            # Assign current char to index i
            chars[i] = current_char_code
            
            # Propagate this character to all j where lcp[i][j] > 0
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    # If j was already assigned a different character, contradiction
                    if chars[j] != -1 and chars[j] != current_char_code:
                        return ""
                    chars[j] = current_char_code
            
            current_char_code += 1
            
        # Convert integer codes to actual string
        word = "".join(chr(code + ord('a')) for code in chars)
        
        # 3. Verify the constructed string generates the exact input LCP matrix
        # We compute the LCP matrix from 'word' using DP to compare
        # dp[i][j] stores the lcp of word[i:] and word[j:]
        # To save space, we can just compute and compare on the fly or build a matrix
        # Building a matrix is clearer for comparison
        
        # Initialize computed_lcp with zeros
        computed_lcp = [[0] * n for _ in range(n)]
        
        # Fill DP table from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        computed_lcp[i][j] = 1 + computed_lcp[i+1][j+1]
                    else:
                        computed_lcp[i][j] = 1
                else:
                    computed_lcp[i][j] = 0
                    
                # Early mismatch check
                if computed_lcp[i][j] != lcp[i][j]:
                    return ""
                    
        return word
