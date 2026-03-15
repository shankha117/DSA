#!/usr/bin/env python3
"""
Minimum Subset Sum Difference

Given an array of positive integers, partition it into two subsets such that
the absolute difference of their sums is minimized. Return that minimum difference.

Approach:
- Let total be the sum of all elements. If we can achieve some subset sum `s` (0 <= s <= total // 2),
  then the other subset sum is `total - s`. The difference will be `abs((total - s) - s) = total - 2*s`.
- Therefore, we want the achievable subset sum `s` that is as close as possible to `total // 2`.
- Compute the set of achievable sums using classic 0/1 subset-sum DP over sums up to total // 2.
- Answer is min(total - 2*s) over all achievable `s` in [0, total // 2].

Time complexity: O(n * total_sum)
Space complexity: O(total_sum)
Where total_sum is the sum of all elements and n is the number of elements.
"""

from typing import List


def min_subset_sum_difference(nums: List[int]) -> int:
    """
    Compute the minimum possible difference between the sums of two subsets.

    Args:
        nums: List of positive integers.

    Returns:
        Minimum absolute difference of sums between two subsets.

    Examples:
        >>> min_subset_sum_difference([1, 2, 3, 9])
        3
        # One optimal partition: {1,2,3} sum=6 and {9} sum=9 -> |9-6|=3

        >>> min_subset_sum_difference([1, 2, 7])
        4
        # One optimal partition: {1,7} sum=8 and {2} sum=2 -> |8-2|=6 (not minimal)
        # Better: {2,7} sum=9 and {1} sum=1 -> |9-1|=8 (still not minimal)
        # Best: {1,2} sum=3 and {7} sum=7 -> |7-3|=4

        >>> min_subset_sum_difference([3, 1, 4, 2, 2, 1])
        1
        # Optimal partition difference is 1
    """
    if not nums:
        return 0

    total = sum(nums)
    target = total // 2

    # dp[s] indicates whether sum s is achievable using some subset of nums.
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Traverse backward to avoid reusing the same item multiple times.
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    # Find the achievable sum closest to target.
    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2 * s

    # Fallback; theoretically unreachable since dp[0] is always True.
    return 0


def _min_subset_sum_difference_bitset(nums: List[int]) -> int:
    """
    Alternative bitset-based implementation that can be faster in practice.

    Uses a bitset where bit i indicates whether sum i is achievable.
    """
    if not nums:
        return 0
    total = sum(nums)
    target = total // 2

    bitset = 1  # only sum 0 achievable
    for num in nums:
        bitset |= bitset << num

    # Find achievable s <= target closest to target
    for s in range(target, -1, -1):
        if (bitset >> s) & 1:
            return total - 2 * s
    return 0


if __name__ == "__main__":
    # Simple manual tests
    tests = [
        ([1, 2, 3, 9], 3),
        ([1, 2, 7], 4),
        ([3, 1, 4, 2, 2, 1], 1),
        ([], 0),
        ([5], 5),
        ([1, 1, 1, 1], 0),
        ([2, 2, 2, 2, 2], 0),
        ([1, 6, 11, 5], 1),  # classic example
    ]

    for arr, expected in tests:
        res_tab = min_subset_sum_difference(arr)
        res_bit = _min_subset_sum_difference_bitset(arr)
        print(f"nums={arr}, tab_dp={res_tab}, bitset={res_bit}, expected={expected}")
