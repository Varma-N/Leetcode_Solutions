# Problem 3016: Minimum Number of Pushes to Type Word II

## Intuition
The key to solving this problem lies in understanding the relationships between the letters of the word and the keys on the telephone keypad.  We can determine the minimum number of pushes by efficiently mapping the letters to the keys, minimizing the total number of times each key is pushed.


## Approach
1. **Counting Letter Occurrences:**
   -  Use a `Counter` object (or a similar data structure) to store the frequency of each letter in the input word. This will help us determine how many times each letter needs to be pushed.

2. **Sorting Letter Counts:**
   - Sort the letter counts in descending order using `sorted(counts.values(), reverse=True)`. This will help us determine the most frequently occurring letters (those we'll need to push the keys for). 
   - The most frequently occurring letters will represent the most efficient mapping. 
   - We'll use these counts to determine the number of times keys will be pushed.

3. **Calculating Total Pushes:**
   - For each letter's occurrence (sorted by counts), calculate the number of pushes required by the following logic:
      - We use the following formula to calculate the number of pushes: `total_pushes += count * ((i // 8) + 1)`
   - The logic behind this formula is based on the frequency of the letter. A higher frequency of a letter means it will need to be pushed more times. 
   - We use the `//` operator to get the whole number of times the letter needs to be pushed and then add it to the total number of pushes.

4. **Return:** Return the total number of pushes required to type the word.


## Complexity Analysis
* **Time Complexity:** $O(N)$ - The main operations involve iterating through the word's character frequency.  The sorting will have a time complexity of $O(N\log(N))$,
* **Space Complexity:** $O(N)$ - We'll use a `Counter` object to store the letter counts, which will have space complexity proportional to the number of letters in the word.