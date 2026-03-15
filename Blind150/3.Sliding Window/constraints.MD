Here’s the **short, exam-ready rulebook** 👇

---

## ✅ You **CAN** use Sliding Window when

### Core constraints

* ✅ Array / string is **linear**
* ✅ Window expansion **monotonically increases** some metric
* ✅ Window shrink **monotonically decreases** that metric
* ✅ Usually **no negative numbers** (or effect is predictable)

---

### Typical patterns

| Problem type                | Constraint                |
| --------------------------- | ------------------------- |
| Fixed-size window           | Window size = `k`         |
| Variable-size window        | All numbers **≥ 0**       |
| Longest / shortest subarray | Condition is monotonic    |
| At most / at least `k`      | Count/frequency based     |
| Strings                     | Characters (no negatives) |

---

## 🧠 One-line rule

> **If expanding the window can reduce the value you’re tracking → sliding window fails.**

---


### Examples (✅ Sliding Window)

* Max / min sum of subarray of size `k`
* Longest substring without repeating characters
* Longest substring with at most `k` distinct chars
* Minimum window substring
* Longest subarray with sum ≤ `k` (nums ≥ 0)
* Average of subarrays of size `k`

---

## ❌ You **CANNOT** use Sliding Window when

### Breaking constraints

* ❌ **Negative numbers** affect sum unpredictably
* ❌ Need to count **all** valid subarrays
* ❌ Window sum is **non-monotonic**
* ❌ Order matters globally (prefix dependencies)

---

### Examples (❌ No Sliding Window)

* Subarray sum equals `k` (with negatives)
* Count of subarrays with sum = `k`
* Max subarray sum (Kadane’s instead)
* Prefix-sum / hashmap based problems
* “Number of subarrays” problems (usually)

---



If you want, I can give you a **1-page LeetCode mapping (problem → pattern)** to memorize fast 🚀
