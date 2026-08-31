class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_int = 0
        digit_sum = 0
        for digit in str(n):
            num = int(digit)
            digit_sum += num
            if num > 0:
                new_int = new_int * 10 + num
        return new_int * digit_sum

        