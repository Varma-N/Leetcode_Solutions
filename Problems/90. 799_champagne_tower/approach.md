# Champagne Tower

## Problem Overview

We are tasked with simulating the flow of champagne through a pyramid of glasses. 
- The tower starts with one glass at the top (row 0).
- Each subsequent row has one more glass than the previous row.
- Each glass can hold exactly **1 unit** of champagne.
- Any amount poured into a glass that exceeds 1 unit flows equally to the two glasses directly below it (left and right).
- Given the total amount poured and a specific query coordinate (row, glass), we need to determine how much liquid is in that specific glass.

## Intuition

This problem can be modeled using **Dynamic Programming** or a direct **Simulation** approach. 

Think of the tower as a 2D grid. When we pour liquid into the top glass, if it overflows, that overflow is distributed to the next row. The amount of liquid in any given glass depends entirely on the overflow from the glasses directly above it. 

Since the flow only moves downwards (from row `i` to row `i+1`), we can process the tower row by row. We don't need to simulate time steps; we just need to calculate the final stable state of the liquid distribution up to the queried row.

## Step-by-Step Approach

1.  **Initialize a Data Structure**:
    Create a 2D array (or table) to represent the tower. The size should be sufficient to cover the `query_row`. Initialize all values to 0.0.

2.  **Pour the Liquid**:
    Place the entire `poured` amount into the topmost glass (position `[0][0]`).

3.  **Simulate the Flow**:
    Iterate through each row from the top down to the `query_row`.
    - For each glass in the current row:
        - Check if the glass contains more than 1 unit of liquid.
        - **If it does not overflow**: The liquid stays in the glass. No action is needed for the next row regarding this glass.
        - **If it overflows**:
            - Calculate the excess amount (current amount - 1).
            - Cap the current glass at exactly 1 unit.
            - Distribute half of the excess to the glass directly below-left.
            - Distribute half of the excess to the glass directly below-right.

4.  **Handle the Result**:
    After processing all rows up to the `query_row`, look at the value in the table at `[query_row][query_glass]`.
    - Since a glass cannot hold more than 1 unit, if the value is greater than 1, return 1.
    - Otherwise, return the calculated value.

## Complexity Analysis

Let $R$ be the `query_row`.

### Time Complexity
- We iterate through each row from 0 to $R$.
- For each row $i$, there are $i + 1$ glasses.
- The total number of glasses processed is roughly the sum of integers from 1 to $R$, which is $\frac{R(R+1)}{2}$.
- Therefore, the time complexity is **$O(R^2)$**.

### Space Complexity
- We use a 2D array to store the amount of liquid in each glass up to the `query_row`.
- Similar to the time complexity, the number of elements stored is proportional to the number of glasses in the triangle up to row $R$.
- Therefore, the space complexity is **$O(R^2)$**.

*(Note: Since the problem constraints typically limit the query row to a small number like 100, this quadratic complexity is highly efficient and well within limits.)*
