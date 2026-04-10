class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case: empty string
        if not s:
            return ""
        
        substrings = []
        balance = 0
        start = 0
        
        # Decompose s into primitive special substrings
        for i, char in enumerate(s):
            if char == '1':
                balance += 1
            else:
                balance -= 1
            
            # When balance hits 0, we found a primitive special substring
            if balance == 0:
                # Extract the substring s[start...i]
                # It is guaranteed to start with '1' and end with '0'
                # Recursively solve for the inside part s[start+1...i-1]
                inner = self.makeLargestSpecial(s[start+1 : i])
                substrings.append("1" + inner + "0")
                start = i + 1
        
        # Sort the substrings in descending order to maximize lexicographical value
        substrings.sort(reverse=True)
        
        # Join and return
        return "".join(substrings)
