## Approach: Greedy Sorting

**1. Understand the Optimal Strategy**
To minimize the total amount spent, we need to maximize the value of the free candies we receive. The problem states that the free candy must cost less than or equal to the minimum of the two purchased candies. 
Therefore, to get the most expensive candies for free, we should always buy the most expensive candies available in pairs. This allows us to claim the next most expensive available candy for free.

**2. Sort the Array**
Sort the `cost` array in **descending** (decreasing) order. By doing this, the most expensive candies are at the front of our list.

**3. Handle Base Cases**
Check the total number of candies. If there are 2 or fewer candies in the array, we cannot get any for free. We simply sum up their costs and return the total immediately.

**4. Group the Candies**
Initialize a variable to keep track of the total cost. Iterate through the sorted candy array in chunks of 3. 

**5. Calculate the Cost per Group**
For every group of 3 candies:
*   We "buy" the first two candies in the group (which are the most expensive remaining ones). Add their costs to the total.
*   We take the third candy in the group for "free" (which is guaranteed to be valid because it is smaller than or equal to the first two, thanks to our descending sort). We simply skip adding its cost to our total.
*   *Note: If the final group has fewer than 3 candies (e.g., just 1 or 2 left), we just pay for whatever is remaining in that chunk.*

**6. Return the Result**
Once the loop finishes processing all the groups, the total cost variable will hold the minimum possible cost. Return this value.