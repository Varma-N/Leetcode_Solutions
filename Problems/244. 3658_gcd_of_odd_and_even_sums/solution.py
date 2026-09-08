class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        # def gcd(a, b):
        #     while b:
        #         a, b = b, a % b
        #     return abs(a)

        # odd_sum = 0
        # even_sum = 0
        # for i in range(1, (n * 2) + 1):
        #     if i & 1:
        #         odd_sum += i
        #     else:
        #         even_sum += i

        # return gcd(odd_sum, even_sum)
