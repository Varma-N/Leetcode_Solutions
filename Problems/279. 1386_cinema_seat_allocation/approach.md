```markdown
# Problem 1386: Cinema Seat Allocation

## Intuition
The key is to understand that the maximum number of groups can be found by considering the availability of seat blocks.  By analyzing the reserved seats and their corresponding bitmasks, we can determine the potential number of groups that can be seated in each row.

## Approach
1. **Bitmask Representation:** 
   - Represent each row as a bitmask. A bit represents the reserved status of a seat:
     - `1` represents reserved.
     - `0` represents free.
2. **Initialization:**
   - `reserved_map`: Use a dictionary to store the bitmask representation of each row.  
   - `max_groups`:  Start with `(n - len(reserved_map)) * 2` to account for the maximum number of groups that can be assigned to free seats.
3. **Block Analysis:**
   - For each row, use bitwise operations to determine the available seat blocks:
     - `(mask & 60) == 0`: Check if the left block (2, 3, 4, 5) is free. 
     - `(mask & 960) == 0`: Check if the right block (6, 7, 8, 9) is free.
     - `(mask & 240) == 0`: Check if the middle block (4, 5, 6, 7) is free.  
   - Increment `max_groups` if one of these blocks is free.
4. **Return Value:**
   - Return the calculated `max_groups`.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * Iterating through the `reservedSeats` list.  We perform a constant number of operations per row.
* **Space Complexity:** $O(1)$
    * We only use a dictionary, `reserved_map`, which uses constant space.


```

---

**