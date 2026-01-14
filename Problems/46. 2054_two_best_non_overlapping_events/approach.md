# 2054. Two Best Non-Overlapping Events

## Problem Summary

You are given a list of events where each event is represented as:

[startTime, endTime, value]

You may attend **at most two events**, and the selected events must **not overlap**. Two events are considered non-overlapping if the first event ends **strictly before** the second event starts.

The objective is to return the **maximum possible sum of values** from at most two such events.

---

## High-Level Idea

For every event, we want to know:
- What is the **best event that ended before this one starts?**

If we can answer this efficiently, then for each event we can:
- Take it alone, or
- Combine it with the best compatible past event

To achieve this efficiently, we use:
- **Sorting**
- **A min-heap (priority queue)**
- **Greedy accumulation of the best past value**

---

## Step-by-Step Walkthrough

### 1. Sort Events by Start Time

We first sort all events by their `startTime`.

This allows us to process events in chronological order and ensures that when we are handling a current event, all possible compatible past events appear before it in the list.

---

### 2. Use a Min-Heap to Track Active Events

We maintain a **min-heap** where each entry is:

(endTime, value)

The heap is ordered by `endTime`, so the event that finishes the earliest is always at the top.

This helps us efficiently remove events that can no longer overlap with future events.

---

### 3. Track the Best Past Event

We keep a variable:

best_past_value

This represents the **maximum value of any event that has already ended** and is therefore compatible with the current event.

Whenever an event is removed from the heap (because it ended before the current event starts), we update:

best_past_value = max(best_past_value, removed_event_value)

---

### 4. Process Each Event

For each event [start, end, value]:

1. Remove all events from the heap whose `endTime < start`
2. Update `best_past_value` using the removed events
3. Compute the best possible sum:
   - Either take the current event alone
   - Or combine it with `best_past_value`
4. Update the global maximum answer
5. Push the current event into the heap

This guarantees that every valid pair of non-overlapping events is considered.

---

### 5. Return the Result

After processing all events, the stored maximum value is the answer.

---

## Example Walkthrough

Input:
`events = [[1,3,2],[2,4,3],[4,5,2]]`

Sorted by start time:
`[[1,3,2],[2,4,3],[4,5,2]]`

Processing:
- Event [1,3,2]: no past events → max = 2
- Event [2,4,3]: overlaps with previous → max = 3
- Event [4,5,2]:
  - [1,3,2] is removed (ends before 4)
  - best_past_value = 2
  - sum = 2 + 2 = 4 → max updated

Output: 4


---

## Why This Approach Works

- Each event is added and removed from the heap **once**
- The heap guarantees efficient access to the earliest-ending events
- Greedily tracking the best past value ensures optimal pairing
- All valid non-overlapping combinations are evaluated

---

## Complexity Analysis

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

This approach is efficient and well within the problem constraints.
