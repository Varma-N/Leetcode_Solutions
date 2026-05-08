class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_count = 3 * (2 ** (n - 1))
        if k > total_count:
            return ""
        
        result = []
        chars = ['a', 'b', 'c']

        for i in range(n):
            bucket_size = 2 ** (n - 1 - i)
            
            for char in chars:
                if result and result[-1] == char:
                    continue
                
                if k <= bucket_size:
                    result.append(char)
                    break 
                else:
                    k -= bucket_size
                    
        return "".join(result)
        
