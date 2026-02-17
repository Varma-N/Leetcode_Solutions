# 2943. Maximize Area of Square Hole in Grid

## 🧠 Approach

To maximize the area of a square hole in the grid, we need to understand how removing consecutive horizontal and vertical bars affects the size of the hole.

### 🔎 Key Insight

- Removing `k` consecutive bars creates a gap of size `k + 1`.
- To form a square hole:
  - We need the **maximum consecutive horizontal bars removed**
  - And the **maximum consecutive vertical bars removed**
- The side of the largest square is:

```
side = min(max_consecutive_horizontal + 1, max_consecutive_vertical + 1)
```

- The area is:

```
area = side × side
```

---

## 🚀 Algorithm

1. Sort the list of removed bars.
2. Find the longest sequence of consecutive integers.
3. Add `1` to the longest consecutive count (because removing `k` bars creates a gap of `k + 1`).
4. Compute this for both:
   - `hBars`
   - `vBars`
5. The square side length is the minimum of the two spans.
6. Return `side * side`.

---

## ⏱ Time Complexity

Let:
- `H = len(hBars)`
- `V = len(vBars)`

Sorting takes:

```
O(H log H + V log V)
```

The consecutive scan takes:

```
O(H + V)
```

### ✅ Final Time Complexity:

```
O(H log H + V log V)
```

---

## 💾 Space Complexity

We only use a few variables and sort in place.

### ✅ Final Space Complexity:

```
O(1)
```

(ignoring sorting space depending on implementation)

---

## 🎯 Final Result

- Find longest consecutive removed bars
- Add 1 to get gap size
- Take minimum of horizontal and vertical gap
- Return square of that value

Efficient and clean solution 🚀
