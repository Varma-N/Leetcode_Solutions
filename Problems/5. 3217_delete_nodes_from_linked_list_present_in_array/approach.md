# 💡 Problem #3217: Delete Nodes From Linked List Present in Array
**Link:** [LeetCode #3217](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/)

---

## 🧠 Approach

### 🔍 Problem Understanding
You’re given:
- A **singly linked list** `head`.
- An integer array `nums`.

You must **remove every node** from the linked list whose value appears in `nums`, and return the head of the modified list.

---

### ⚙️ Intuition
- Lookups like “is this value in `nums`?” should be **O(1)**.  
  → Convert `nums` to a `set` for constant-time membership checks.
- Deleting nodes in a singly linked list is easiest with a **dummy (sentinel) node** to handle deletions at the head cleanly.

---

## 🧩 Step-by-Step Strategy
1. Convert `nums` into a `set` → `num_set`.
2. Create `dummy = ListNode(0)` and set `dummy.next = head`.
3. Use a pointer `current = dummy`.
4. Traverse while `current.next` exists:
   - If `current.next.val` is in `num_set`, **skip** the node: `current.next = current.next.next`.
   - Else, **advance**: `current = current.next`.
5. Return `dummy.next` as the new head.

---

## 🧠 Why This Works
- Using a dummy node avoids edge cases when the **head itself must be deleted**.
- Using a set gives **O(1)** checks for whether to delete a node.
- Single pass over the list gives optimal linear time.

---

## ⏱️ Complexity
- **Time:** `O(n + m)` where `n` = number of nodes in the list, `m` = length of `nums` (to build the set).  
- **Space:** `O(m)` for the set.

---

## 🧪 Example
**Input:**  
- `head = [1, 2, 3, 4, 5]`  
- `nums = [2, 5]`

**Process:**  
- Delete nodes with values `2` and `5`.

**Output:**  
- `[1, 3, 4]`

---

✅ **Key Insight:**  
Use a **dummy node** to simplify deletions and a **set** for fast membership checks.
