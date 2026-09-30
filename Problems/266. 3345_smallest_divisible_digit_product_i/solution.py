class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        curr = n
        
        while True:
            temp = curr
            digit_product = 1
            
            while temp > 0:
                digit = temp % 10
                digit_product *= digit
                temp //= 10
            if digit_product % t == 0:
                return curr
            curr += 1