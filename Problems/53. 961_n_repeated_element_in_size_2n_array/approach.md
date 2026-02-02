# Approach — 961. N-Repeated Element in Size 2N Array

## 🔍 Problem Understanding

You are given an array `nums` of size `2N` where:

- Exactly **one element is repeated `N` times**
- All other elements appear **only once**

The goal is to find and return the element that is repeated `N` times.

---

## 💡 Key Observation

Since the repeated element appears **half of the array size**, it is guaranteed to appear **at least twice early** in the array.

This allows us to detect the repeated element **as soon as we encounter it again**.

---

## 🧠 Strategy

We iterate through the array and keep track of elements we have already seen.

- If an element has been seen before → it must be the `N`-repeated element
- Return it immediately
- No need to count frequencies explicitly

---

## 🚀 Algorithm Steps

1. Initialize an empty hash map (or set) called `seen`
2. Traverse each element in `nums`
3. If the element already exists in `seen`, return it
4. Otherwise, store the element in `seen`

---
## ⏱ Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)
