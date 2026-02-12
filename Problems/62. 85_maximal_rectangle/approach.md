# Maximal Rectangle – Step-by-Step Approach

## 1. Understand the Problem
You are given a 2D binary matrix filled with `"0"` and `"1"`.  
Your task is to find the **largest rectangle containing only `1`s** and return its area.

- The rectangle must be fully filled with `1`s
- Rows and columns must be contiguous

---

## 2. Core Insight
This problem can be reduced to a series of **Largest Rectangle in Histogram** problems.

Instead of analyzing the matrix directly:
- Treat **each row as the base of a histogram**
- Build heights of consecutive `1`s column by column
- For each row’s histogram, compute the largest rectangle area

---

## 3. Histogram Construction
Maintain an array called `heights` with size equal to the number of columns.

For each row:
- If the current cell is `"1"`, increase the height of that column by 1
- If the current cell is `"0"`, reset the height to 0

This converts each row into a histogram representing vertical stacks of `1`s.

---

## 4. Why Histograms Work
Each histogram represents all rectangles that **end at the current row**.

By solving the largest rectangle in this histogram:
- You automatically consider all rectangles of `1`s that use this row as the bottom boundary

---

## 5. Largest Rectangle in Histogram (Using Stack)
For the current histogram:
- Use a **monotonic increasing stack** to store column indices
- Traverse columns from left to right
- Add a virtual bar of height `0` at the end to flush the stack

### Key Logic:
- When the current height is **smaller** than the height at the stack’s top:
  - Pop from the stack
  - Calculate area using:
    - Height = popped bar height
    - Width = distance between current index and new stack top
  - Update the maximum area

---

## 6. Width Calculation Rule
When a bar is popped:
- If the stack is empty:
  - Width = current index
- Otherwise:
  - Width = current index − stack top − 1

This ensures the rectangle spans only valid columns.

---

## 7. Track the Global Maximum
- After processing each row’s histogram, update the global maximum area
- Continue until all rows are processed

---

## 8. Final Answer
The largest rectangle area found during all histogram evaluations is the answer.

---

## 9. Time and Space Complexity
- **Time Complexity:** `O(rows × cols)`
  - Each element is pushed and popped at most once per row
- **Space Complexity:** `O(cols)`
  - For the histogram and stack

---

## 10. Why This Approach Is Optimal
- Converts a 2D problem into multiple 1D problems
- Uses stack-based processing for linear-time histogram evaluation
- Efficient and widely used for rectangle-related matrix problems

---

This structured approach is ideal for explaining the solution clearly in a GitHub markdown file.
