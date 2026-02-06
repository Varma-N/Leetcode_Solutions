# Maximum Level Sum of a Binary Tree

## Approach

1. **Handle the edge case**  
   If the binary tree is empty, return `0` since no levels exist.

2. **Use level-order traversal (BFS)**  
   Traverse the tree level by level using a queue. This ensures all nodes at the same depth are processed together.

3. **Track level information**  
   Maintain:
   - A variable to store the maximum level sum encountered so far  
   - A variable to store the level number corresponding to that maximum sum  
   - A counter to track the current level number, starting from 1

4. **Process each level**
   - Determine how many nodes are present at the current level (queue size)
   - Iterate through these nodes and accumulate their values into a level sum
   - Add each node’s left and right children to the queue for the next level

5. **Update the result**
   - After processing a level, compare its sum with the current maximum
   - If the current level’s sum is greater, update the maximum sum and record the current level number
   - In case of equal sums, no update is needed, ensuring the smallest level number is preserved

6. **Continue until traversal is complete**  
   Repeat the process until all levels of the tree have been traversed.

7. **Return the answer**  
   Return the level number that has the maximum sum of node values.

---

## Time and Space Complexity

- **Time Complexity:** `O(n)`  
  Each node in the binary tree is visited exactly once.

- **Space Complexity:** `O(w)`  
  Where `w` is the maximum width of the binary tree, corresponding to the maximum number of nodes stored in the queue at any level.
