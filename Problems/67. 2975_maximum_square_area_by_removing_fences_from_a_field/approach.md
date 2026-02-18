# 2975. Maximum Square Area by Removing Fences From a Field  

## 🧠 Problem Understanding

We are given:

- A field of size **m × n**
- Lists of removable **horizontal fences** and **vertical fences**
- The outer boundary fences at positions `1` and `m` (horizontal) and `1` and `n` (vertical) always exist  

Our goal is to:

- Remove fences in such a way that we form the **largest possible square**
- Return the **area** of that square
- If no square can be formed, return `-1`
- Since the result may be large, return it modulo **10⁹ + 7**

---

## 🚀 Step-by-Step Approach

### Step 1: Include Boundary Fences

Even if not provided, the fences at:
- Horizontal: `1` and `m`
- Vertical: `1` and `n`

must always be considered.

So:
- Add `1` and `m` to the horizontal fences list
- Add `1` and `n` to the vertical fences list

Then sort both lists.

---

### Step 2: Compute All Possible Vertical Distances

To form a square, we need equal horizontal and vertical side lengths.

1. For every pair of vertical fences:
   - Compute the distance between them.
   - Store all possible distances in a **set**.

Why a set?
- Fast lookup (`O(1)`)
- Avoid duplicate distances

Now we have all possible vertical side lengths.

---

### Step 3: Check Horizontal Distances

Next:

1. For every pair of horizontal fences:
   - Compute the distance between them.
2. Check if this distance exists in the vertical distance set.
3. If yes:
   - It means we can form a square with that side length.
   - Update the maximum side found so far.

---

### Step 4: Compute Final Result

- If no matching side length is found → return `-1`
- Otherwise:
  - Return `(max_side × max_side) % (10^9 + 7)`

---

## 🎯 Why This Works

A square requires:

```
horizontal distance == vertical distance
```

So the problem reduces to:

- Find all possible vertical distances.
- Check which horizontal distances match them.
- Take the largest matching value.

---

## ⏱ Time Complexity

Let:

- `H = number of horizontal fences`
- `V = number of vertical fences`

### Computing vertical distances:
```
O(V²)
```

### Computing horizontal distances:
```
O(H²)
```

### Overall Time Complexity:
```
O(H² + V²)
```

---

## 🗂 Space Complexity

- We store all possible vertical distances in a set.
- In the worst case, this could be:

```
O(V²)
```

---

## ✅ Summary

- Add boundary fences.
- Compute all vertical gaps.
- Match horizontal gaps against vertical gaps.
- Track maximum valid square side.
- Return area modulo `10^9 + 7`.
- Return `-1` if no square exists.
