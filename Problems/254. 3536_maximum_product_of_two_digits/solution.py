class Solution:
    def maxProduct(self, n: int) -> int:
        highest = -1
        second_highest = -1

        for char in str(n):
            digit = int(char)
            if digit > highest:
                second_highest = highest
                highest = digit
            elif digit > second_highest <= highest:
                second_highest = digit
        return highest*second_highest
            
        