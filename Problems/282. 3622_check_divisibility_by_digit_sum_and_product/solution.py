class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product_of_digits = 1
        sum_of_digits = 0
        digits = 0
        temp = n
        while temp > 0:
            digits = temp % 10
            sum_of_digits += digits
            product_of_digits *= digits
            temp //= 10
        return n % (product_of_digits + sum_of_digits) == 0