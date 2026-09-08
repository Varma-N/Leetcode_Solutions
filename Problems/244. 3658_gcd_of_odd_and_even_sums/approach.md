# Problem 3658: GCD of Odd and Even Sums

## Intuition
The core idea is that the GCD of two sums can be calculated by finding the GCD of the sums of the odd and even numbers. 
This is because the GCD of any two numbers is the same as the GCD of their remainders when divided by a common factor. For example, the GCD of 12 and 18 is 6.

## Approach
1. **Calculate the sums of odd and even numbers:** We need to find the sum of the smallest n positive odd numbers and the sum of the smallest n positive even numbers.
2. **Use GCD:** We know that the GCD of two numbers is the same as the GCD of their remainders when divided by a common factor. Therefore, we can use the GCD of the sum of odd numbers and sum of even numbers to find the GCD of the original numbers.

**Example Breakdown**
 
Let's break down the algorithm for n = 4:

1. **Odd Sum Calculation:**
   * We need to sum the first n odd numbers.
   * The first n odd numbers are 1, 3, 5, 7... 
   * We add these numbers to get the odd sum. 

2. **Even Sum Calculation:**
   * We need to sum the first n even numbers.
   * The first n even numbers are 2, 4, 6, 8... 
   * We add these numbers to get the even sum. 


3. **GCD Calculation:**
   * We find the GCD of the odd sum and the even sum.

**Time Complexity:** $O(n)$
* We are adding a number of numbers in each step, so the time complexity is linear. 

**Space Complexity:** $O(1)$
* We are only using a few variables for the sum. 



```
