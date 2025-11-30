# 💡 Problem #757: Set Intersection Size At Least Two
**Link:** https://leetcode.com/problems/set-intersection-size-at-least-two/

---

## 🧠 Problem Understanding

You are given a list of intervals.  
You must choose a set of integers **S** such that:

➡️ **Every interval contains at least TWO numbers from S**  
➡️ You want to minimize `|S|` (the size of the chosen set).

---

## ⚙️ Key Insight — Classic Greedy Interval Logic

This is a **minimum hitting set** problem with a twist:  
Instead of hitting each interval with **at least 1 point**, we must hit it with **at least 2 points**.

The optimal strategy is:

### 📌 Sort intervals by:
1. **End increasing**
2. If tie → **Start decreasing**

This sorting ensures:
- We try to satisfy intervals ending earlier first.
- Larger start is processed first when ends tie → reduces conflicts.

---

## 🧩 Greedy Strategy

We maintain the **two largest chosen points so far**:

- p1 = second largest chosen point
- p2 = largest chosen point


For each interval `[start, end]`:

### Case 1️⃣ → Interval has **no intersection** with {p1, p2}

`p2 < start`

We need **two new points**:
- Choose the largest possible → `end - 1` and `end`
`p1 = end - 1`
`p2 = end`
`result += 2`

### Case 2️⃣ → Interval has **only one of {p1, p2}**
`p1 < start <= p2`

We need **one more point**:
- Pick the largest possible → `end`
`p1 = p2`
`p2 = end`
`result += 1`

### Case 3️⃣ → Interval already has **both points**
`p1 >= start`

Do nothing — this interval is already satisfied.

---

## 🧠 Why This Works

- Picking the **largest possible points** inside an interval is optimal because:
  - They have the highest chance of hitting future intervals.
- Sorting by `end ASC, start DESC` ensures:
  - Earlier-ending intervals are handled first (tightest constraints).
  - For equal endings, intervals with larger start are processed first to preserve optimality.

This is a well-known greedy pattern for k-intersection interval problems.

---

## 🧮 Example

```
intervals = [[1,3], [1,4], [2,5], [3,5]]

After sorting:
[1,3], [2,5], [3,5], [1,4]

Processing:
[1,3] → p2 < start → add {2,3}
[2,5] → p1 >= start → already have {2,3} inside
[3,5] → p1 >= start → already have {2,3} inside
[1,4] → p1 >= start → already have {2,3} inside

Answer = 2
```

---

## ⏱️ Complexity

- **Time:** O(n log n) for sorting  
- **Space:** O(1)

---

## 🔑 Key Insight  
Always insert the **largest possible points** for each interval, and sort intervals to ensure the greedy choices remain globally optimal.
