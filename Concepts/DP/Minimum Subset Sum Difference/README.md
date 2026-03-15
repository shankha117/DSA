# Minimum Subset Sum Difference

Partition a set of positive integers into two subsets such that the absolute difference of their sums is minimized. Return that minimum difference.

- Directory: `DSA/Concepts/DP/Minimum Subset Sum Difference`
- Language solutions:
  - `Python/min_subset_sum_diff.py`
  - `Go/min_subset_sum_diff.go`

## Problem Statement

Given an array `nums` of positive integers, split it into two subsets `S1` and `S2` such that the value `|sum(S1) - sum(S2)|` is minimized. Output this minimum possible difference.

Constraints:
- `1 <= len(nums) <= N` (depends on your usage)
- `1 <= nums[i]`
- All numbers are positive integers

Examples:
- `nums = [1, 2, 3, 9]` -> Minimum difference is `3`
- `nums = [1, 2, 7]` -> Minimum difference is `4`
- `nums = [3, 1, 4, 2, 2, 1]` -> Minimum difference is `1`
- `nums = [1, 6, 11, 5]` -> Minimum difference is `1`

## Key Insight

Let `total = sum(nums)`. If a subset sum `s` is achievable (with `0 <= s <= total // 2`), the other subset has sum `total - s`, and the difference is:

`diff = abs((total - s) - s) = total - 2 * s`

Therefore, the problem reduces to finding an achievable subset sum `s` that is as close as possible to `total // 2`.

## Approaches

### 1) 0/1 Subset-Sum DP (Boolean Table)

- Maintain a boolean DP array `dp` of size `target + 1` where `target = total // 2`.
- `dp[s]` indicates whether a subset with sum `s` is achievable.
- Initialize `dp[0] = True`.
- For each `num` in `nums`, update `dp` backwards: `for s in [target..num]`, set `dp[s] |= dp[s - num]`.
- After processing, scan `s` from `target` down to `0` and take the first `s` where `dp[s] == True`.
- Answer is `total - 2 * s`.

Complexity:
- Time: `O(n * total)` where `total = sum(nums)`
- Space: `O(total)`

This is typically the most straightforward implementation and works well for moderate sums.

### 2) Bitset-Based DP (Optimized Bit Operations)

- Represent achievable sums via a bitset where bit `i` means sum `i` is achievable.
- Start with bitset having only bit `0` set.
- For each `num`, left-shift the bitset by `num` and OR it back into the bitset.
- Scan from `target` downwards to find the closest achievable `s`.

Complexity:
- Time: roughly `O(n * total / word_size)`
- Space: `O(total)`

This approach can be faster in practice due to word-level operations, but requires careful handling to avoid overflow and may use a dynamic bitset representation for large totals.

## Python Implementation

See `Python/min_subset_sum_diff.py` for both the boolean DP and bitset implementations, along with simple test cases.

Reference snippet:
```DSA/Concepts/DP/Minimum Subset Sum Difference/Python/min_subset_sum_diff.py#L1-40
#!/usr/bin/env python3
"""
Minimum Subset Sum Difference
...
def min_subset_sum_difference(nums: List[int]) -> int:
    ...
    total = sum(nums)
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2 * s
    return 0
```

Alternative bitset method in the same file:
```DSA/Concepts/DP/Minimum Subset Sum Difference/Python/min_subset_sum_diff.py#L42-84
def _min_subset_sum_difference_bitset(nums: List[int]) -> int:
    ...
    bitset = 1  # only sum 0 achievable
    for num in nums:
        bitset |= bitset << num
    for s in range(target, -1, -1):
        if (bitset >> s) & 1:
            return total - 2 * s
    return 0
```

## Go Implementation

See `Go/min_subset_sum_diff.go` for both the boolean DP and a dynamic-bitset approach, along with test cases in `main()`.

Reference snippet:
```DSA/Concepts/DP/Minimum Subset Sum Difference/Go/min_subset_sum_diff.go#L1-52
// MinSubsetSumDifference computes the minimum difference via 0/1 DP.
func MinSubsetSumDifference(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    total := 0
    for _, v := range nums {
        total += v
    }
    target := total / 2
    dp := make([]bool, target+1)
    dp[0] = true
    for _, num := range nums {
        for s := target; s >= num; s-- {
            if dp[s-num] {
                dp[s] = true
            }
        }
    }
    for s := target; s >= 0; s-- {
        if dp[s] {
            return total - 2*s
        }
    }
    return 0
}
```

Dynamic bitset approach:
```DSA/Concepts/DP/Minimum Subset Sum Difference/Go/min_subset_sum_diff.go#L54-128
// MinSubsetSumDifferenceBitset uses a dynamic bitset to track achievable sums.
func MinSubsetSumDifferenceBitset(nums []int) int {
    ...
    // Prepare bitset storage sized to total sum
    words := (total + 64) / 64
    bitset := make([]uint64, words)
    bitset[0] = 1
    // Shift OR for each number
    ...
    for s := target; s >= 0; s-- {
        wordIdx := s / 64
        bitIdx := uint(s % 64)
        if (bitset[wordIdx]>>bitIdx)&1 == 1 {
            return total - 2*s
        }
    }
    return 0
}
```

## Step-by-Step Strategy

1. Compute `total = sum(nums)` and define `target = total // 2`.
2. Use DP to determine achievable sums up to `target`.
3. From `target` down to `0`, find the closest achievable `s`.
4. Compute answer as `total - 2 * s`.

## Edge Cases

- Empty array `[]` -> `0` (difference is zero)
- Single element `[x]` -> `x` (one subset is `[x]`, the other is `[]`)
- All equal elements, even count -> `0`
- Large totals may require more memory; prefer boolean DP for simplicity and robustness.

## Complexity Summary

- Time: `O(n * total)` for the boolean DP, often acceptable for moderate sums.
- Space: `O(total)`.

For very large totals, consider constraints or alternative formulations (e.g., meet-in-the-middle for extremely large inputs), but for typical interview/DSA practice, the above approaches are standard.

## Validation

Example walkthrough for `nums = [1, 6, 11, 5]`:
- `total = 23`, `target = 11`
- Achievable sums include `11` (e.g., subset `[11]`)
- Minimum difference `= 23 - 2 * 11 = 1`

## Files

- `Python/min_subset_sum_diff.py` — Python implementation and tests
- `Go/min_subset_sum_diff.go` — Go implementation and tests
