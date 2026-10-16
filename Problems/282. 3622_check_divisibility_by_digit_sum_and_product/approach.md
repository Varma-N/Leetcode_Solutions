# Problem 3622: Check Divisibility by Digit Sum and Product

## Intuition
Divisibility by a number can often be broken down into the properties of the digits themselves.  The idea is to calculate the sum and product of digits, and then determine if the original number is divisible by the sum and product.  This process can be easily automated.


## Approach
1. **Initialization:** 
   - `product_of_digits = 1` : Initialize the product of digits to 1 as the starting point for calculations.
   - `sum_of_digits = 0`: Initialize the sum of digits to 0 to start counting.
   - `digits = 0`: Initialize the variable to store the last digit of n.
   - `temp = n`: Initialize a temporary variable to store the original number for easy manipulation.
2. **Digit Extraction:**
   - `while temp > 0:`: This loop iterates as long as `temp` is greater than 0.
     - `digits = temp % 10`: Extract the last digit of `temp` using the modulus operator and store it in `digits`.
     - `sum_of_digits += digits`: Add the extracted digit to the `sum_of_digits`.
     - `product_of_digits *= digits`: Multiply the `product_of_digits` by the current digit.
     - `temp //= 10`:  Divide `temp` by 10 to remove the last digit.
3. **Divisibility Check:**
   - `return n % (product_of_digits + sum_of_digits) == 0`:  Check if the original number `n` is divisible by the sum of the product and sum of digits.


## Complexity Analysis
* **Time Complexity:** $O(log(n))$
    * The algorithm iterates through each digit of the number `n`. In each iteration, the time complexity is dominated by the `temp //= 10` operation, which takes constant time. 
* **Space Complexity:** $O(1)$
    * The algorithm uses a fixed amount of space for variables.