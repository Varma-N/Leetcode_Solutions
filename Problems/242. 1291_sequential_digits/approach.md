# Problem 1291: Sequential Digits

## Intuition
The solution leverages the fact that sequential digits in an integer follow a specific pattern.  We start by constructing a string representation of digits (e.g., "123456789"), and iterate through its possible combinations.  For each number in the range [low, high], we examine if the numbers have sequential digits, and append it to the result.  

## Approach
1. **Create a Sample String:**
   - Initialize a string, `sample`, containing the digits 1-9.  
   
2. **Iterate through Potential Numbers:**
   - For each length of the number (from the smallest to the largest) in the range [low_len, high_len], we iterate through the possible starting points for each number. 
   
3. **Construct and Compare:** 
   - For each starting point `start` within the range, construct a new number (`num`) based on the `sample` string. 
   
4. **Check for Sequential Digits:** 
   - For every `num` in the range [low, high], check if the sequence is sequential.  
   
5. **Append to Result:**
   - If the number satisfies the condition (is within the range and has sequential digits), append it to the result list.
 

## Complexity Analysis
* **Time Complexity:** $O(N\cdot\log(N))$
    * The loop iterates through numbers from `low` to `high` in the input, with a maximum number of digits (N) 

* **Space Complexity:** $O(1)$ 
    * We use a constant amount of space, regardless of the input.