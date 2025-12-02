# 💡 Problem #757: Set Intersection Size At Least Two
**Link:** https://leetcode.com/problems/set-intersection-size-at-least-two/

---

## 🧠 Problem Understanding

You are given several intervals.  
Your job is to choose a set **S** of integers such that **every interval contains at least TWO numbers** from this set.

You must **minimize** the size of this set.

This is a classic interval-covering problem, but instead of covering each interval with ≥1 point, we must cover them with **≥2 points**.

---

## ⚙️ Key Insight — Greedy Interval Strategy

To solve it optimally:

### ✔️ Sort the intervals by:
1. **End (ascending)**  
2. If ends tie → **Start (descending)**

Sorting this way ensures:
- We satisfy intervals that “close earlier” first.
- Among equal ends, process intervals with larger starts first → avoids unnecessary additions.

---

## 🧩 Greedy Selection Rules

Maintain:
`p1 = second largest chosen point`
`p2 = largest chosen point`

Process each `[start, end]` interval:

---

### **Case 1:** No overlap with `{p1, p2}`  
Condition:
`p2 < start`

We must add **two new elements**, chosen greedily as the:
`(end - 1) and (end)`
These are the best choices because they maximize coverage for upcoming intervals.

---

### **Case 2:** Exactly one overlap  
Condition:
`p1 < start <= p2`

We need to add **one more element**, again choosing the optimal:
end

This ensures maximum future usefulness.

---

### **Case 3:** Already covered  
Condition:
p1 >= start

Both required points already lie inside interval → do nothing.

---

## 🧮 Example

```
intervals = [[1,3], [1,4], [2,5], [3,5]]

After sorting:
[1,3], [2,5], [3,5], [1,4]

Process:
[1,3] → no overlap → add {2,3}
[2,5] → already has 2,3 → OK
[3,5] → already has 2,3 → OK
[1,4] → already has 2,3 → OK

Answer: 2
```

We need only the set S = {2, 3}.

---

## ⏱️ Complexity

- **Time:** O(n log n) for sorting  
- **Space:** O(1) auxiliary

---

## 🔑 Key Insight  
Always add the **largest possible** new points inside an interval, which maximizes chances of covering future intervals with minimal additions.
