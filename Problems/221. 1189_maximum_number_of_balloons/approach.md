# Approach: Maximum Number of Balloons

## Intuition
The problem asks us to find how many times we can form the word "balloon" using the characters from a given string `text`. Since the order of characters in the original string doesn't matter, this is fundamentally a frequency counting problem. 

To form one instance of the word "balloon", we need exactly:
- 1 'b'
- 1 'a'
- 2 'l's
- 2 'o's
- 1 'n'

The maximum number of words we can form is dictated by the "limiting factor" or bottleneck—the required character that we have the least of.

## Step-by-Step Approach

1. **Initialize a Frequency Map (Hash Map):** 
   We begin by creating an empty dictionary called `counts`. This structure will allow us to map each unique character we encounter to the number of times it appears in the input string.

2. **Populate the Character Counts:** 
   We iterate through the input string `text` character by character. For each character `i`, we update its count in the `counts` dictionary. By using the `dict.get(key, default)` method, we can safely add `1` whether it is the first time we are seeing the character (defaulting to `0`) or we are incrementing an existing count.

3. **Extract Counts for the Target Letters:** 
   We don't care about characters like 'x' or 'z'. We only extract the counts for the specific characters that make up "balloon": 'b', 'a', 'l', 'o', and 'n'. If any of these characters never appeared in the text, `counts.get(char, 0)` safely returns `0`.

4. **Normalize the Counts for Double Letters ('l' and 'o'):** 
   Because the word "balloon" requires two 'l's and two 'o's, having four 'l's only gives us enough for two words. Therefore, we perform integer division by 2 (`// 2`) on the total counts of 'l' and 'o'. This converts the raw character counts into "sets" of double letters available for our target word.

5. **Find the Bottleneck:** 
   At this point, the variables `b`, `a`, `l`, `o`, and `n` represent how many complete words each individual letter could theoretically support. Because we need all of them to form a single word, the overall answer is bottlenecked by the smallest value among them. We use the `min()` function to find and return this limiting value.

## Complexity Analysis

- **Time Complexity:** O(N)
  Where N is the length of the string `text`. We iterate through the string exactly once to populate the frequency dictionary. Retrieving the counts and calculating the minimum are all O(1) constant time operations. 

- **Space Complexity:** O(1)
  Although we use a dictionary to store character frequencies, the maximum number of unique keys it will hold is limited to the 26 lowercase English letters. Since this space requirement does not scale with the size of the input string N, it is considered O(1) constant auxiliary space.