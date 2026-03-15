

# 🧠 A Guide to Solving Interval Problems: Line Sweep vs Segment Trees & More

Interval-based problems frequently appear in coding interviews, competitive programming, and real-world systems like calendars, booking platforms, or CPU schedulers.

---

## ✅ Common Types of Interval Problems

Before choosing an algorithm, it’s useful to categorize the problem:

| Problem Type                | Example                                    |
| --------------------------- | ------------------------------------------ |
| **Merging**                 | Merge overlapping intervals                |
| **Counting**                | How many intervals overlap at a time point |
| **Maximum Overlap**         | Peak number of active intervals            |
| **Range Updates / Queries** | Count updates/queries over ranges          |
| **Dynamic Insert/Delete**   | Insert/remove intervals and query overlap  |

---

## 1. 🧹 Line Sweep Algorithm

### 🔧 Core Idea

* Turn intervals into **events** (start and end).
* Sort events by time.
* Sweep from left to right, keeping track of ongoing intervals.

### ✅ When to Use

Use **Line Sweep** when:

* You only care about **start/end events**.
* You don't need to modify intervals dynamically.
* You want to compute **peak usage**, **overlap counts**, or **merge intervals**.

### 📦 Example Problem

**"Given a list of intervals, find the maximum number of overlapping intervals."**

```python
events = []
for start, end in intervals:
    events.append((start, +1))
    events.append((end, -1))

events.sort()

max_count = count = 0
for _, delta in events:
    count += delta
    max_count = max(max_count, count)
```

### ⏱️ Time Complexity

* Sorting: `O(n log n)`
* Sweep: `O(n)`

---

## 2. 🌲 Segment Tree / Binary Indexed Tree (Fenwick Tree)

### 🔧 Core Idea

* Divide the domain into segments (like \[0, 1e5]).
* Use a tree to efficiently query/update a **range**.
* Supports dynamic updates and range queries in `O(log n)` time.

### ✅ When to Use

Use **Segment Trees** when:

* You need to **frequently update/query** interval counts.
* You deal with **range queries** (e.g., how many intervals cover point `x`).
* Intervals **change over time** (insert/delete).
* Coordinates are integers and can be compressed.

### 📦 Example Problem

**"Given multiple range updates, query how many intervals cover a point `x`."**

```go
// Pseudocode for range update using Segment Tree:
update(start, end, +1)  // Add interval
query(x)                // How many intervals cover x
```

### ⏱️ Time Complexity

* Update/query: `O(log n)`
* Coordinate compression may be needed for large ranges.

---

## 3. 🧮 Prefix Sum (After Coordinate Compression)

### 🔧 Core Idea

* Treat intervals as +1 at `start`, -1 at `end + 1`.
* Build a prefix sum over the compressed coordinate array.

### ✅ When to Use

* All intervals are **known in advance**.
* No dynamic updates.
* You want fast O(1) point queries after O(n log n) preprocessing.

### 📦 Example Problem

**"Count how many intervals cover each point in a fixed list of points."**

```python
timeline = [0] * (max_coord + 2)

for start, end in intervals:
    timeline[start] += 1
    timeline[end + 1] -= 1

for i in range(1, len(timeline)):
    timeline[i] += timeline[i - 1]
```

---

## 4. 🧱 Difference Array

Same idea as prefix sum, optimized for space when doing range updates.
Efficient when you need to apply the **same delta** across many ranges.

---

## 5. 🧭 Interval Tree (Augmented BST)

### 🔧 Core Idea

A binary search tree where each node stores an interval and tracks the **max endpoint** in its subtree.

### ✅ When to Use

* You need to **insert, delete, and query overlapping intervals** in real time.
* Useful for problems like "does any interval overlap with this?"

### 📦 Example Problem

**"Given a stream of intervals, determine if any overlap with a new one."**

Time complexity: `O(log n)` insertion/search

---

## 6. 🧮 Sweep + Heap (for interval scheduling)

### Use when you want:

* The **set of active intervals** at a given time.
* To assign resources like meeting rooms (min-heap of end times).

### 📦 Example

**"Minimum number of meeting rooms required"**

```python
intervals.sort(key=lambda x: x[0])
heap = []

for interval in intervals:
    if heap and heap[0] <= interval[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, interval[1])
```

---

## ✅ When to Use What — Quick Reference

| Problem                                   | Best Approach                |
| ----------------------------------------- | ---------------------------- |
| Count overlaps at points                  | Line Sweep / Prefix Sum      |
| Max concurrent intervals                  | Line Sweep                   |
| Merge intervals                           | Sort + Merge                 |
| Dynamic insert/delete + overlap queries   | Segment Tree / Interval Tree |
| Range updates/point queries               | Segment Tree / BIT           |
| Resource allocation (e.g., rooms)         | Sweep + Min Heap             |
| All intervals known upfront, fast queries | Prefix Sum                   |

---

## ⚠️ Final Tips

* Use **coordinate compression** when values are large (e.g., timestamps).
* Line sweep is often the **simplest** and most performant for fixed datasets.
* Segment Trees are powerful but overkill unless needed for **dynamic** or **range** operations.
* Always consider if intervals are **static** or **dynamic**, and whether queries are **point** or **range**.

---

## 🧪 Practice Problems


| Problem            | Type                 | Algorithm                     | Link                                                                  |
| ------------------ | -------------------- | ----------------------------- | --------------------------------------------------------------------- |
| Insert Interval    | Merge                | Sort + Merge                  | [🔗 LeetCode #57](https://leetcode.com/problems/insert-interval/)     |
| Meeting Rooms II   | Max Overlap          | **Line Sweep + Heap**         | [🔗 LeetCode #253](https://leetcode.com/problems/meeting-rooms-ii/)   |
| Count of Range Sum | Range Count          | Prefix Sum + Divide & Conquer | [🔗 LeetCode #327](https://leetcode.com/problems/count-of-range-sum/) |
| Range Module       | Dynamic Interval Ops | Segment Tree                  | [🔗 LeetCode #715](https://leetcode.com/problems/range-module/)       |
| My Calendar III    | Booking Count        | Line Sweep / Interval Tree    | [🔗 LeetCode #732](https://leetcode.com/problems/my-calendar-iii/)    |

---

Let me know if you’d like this formatted as a Markdown file or broken into slides for teaching.
