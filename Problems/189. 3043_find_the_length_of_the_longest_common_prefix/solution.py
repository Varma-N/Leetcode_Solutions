class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num in arr1:
            s = str(num)
            for i in range(1, len(s)+1):
                prefixes.add(s[:i])
        
        max_length = 0

        for num in arr2:
            s = str(num)
            for i in range(1, len(s)+1):
                if s[:i] in prefixes:
                    max_length = max(max_length, i)
                else: break
        return max_length
            
        