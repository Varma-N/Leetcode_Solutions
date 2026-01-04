# 💡 Problem #2211: Count Collisions on a Road
**Link:** [Problem](https://leetcode.com/problems/count-collisions-on-a-road/)

---

## 🧠 Problem Understanding

You are given a string `directions` representing cars on a one-lane road:

- `'L'` → car moving left
- `'R'` → car moving right
- `'S'` → stationary car

Rules:
- When cars collide, they become **stationary**.
- Cars moving off the road (`L` at far left, `R` at far right) **never collide**.

Goal:
➡️ Count the **total number of collisions** that will occur.

---

## ⚙️ Key Insight

### 1️⃣ Cars that never collide
- Leading `'L'` cars move left forever → **no collision**
- Trailing `'R'` cars move right forever → **no collision**

These can be safely ignored.

---

### 2️⃣ Cars in the middle will collide
After removing:
- Leading `'L'`
- Trailing `'R'`

Every remaining car that is **not `'S'`** will **eventually collide**:
- `'R'` will hit a stationary or left-moving car
- `'L'` will hit a stationary or right-moving car

Each such car contributes **exactly one collision**.

---

## 🧩 Algorithm Steps

1. Skip all leading `'L'` characters.
2. Skip all trailing `'R'` characters.
3. In the remaining middle segment:
   - Count how many cars are **not `'S'`**
4. Return this count.

---

## 🧮 Example

```
directions = "LLRRSLLRSR"

After trimming:
"RRSLLRS"

Non-'S' cars = R, R, L, L, R → 5 collisions
```

---

## 🧠 Why This Works

- Collisions stop further movement.
- Every movable car in the middle must eventually hit something.
- Stationary cars don’t add to the collision count.

This avoids simulating collisions step-by-step.

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## 🔑 Key Insight  
Ignore cars that escape the road; every remaining moving car must collide exactly once.
