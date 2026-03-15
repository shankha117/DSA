package main

import (
	"fmt"
)

// minSubsetSumDiff computes the minimum possible difference between the sums
// of two subsets partitioned from the input array of positive integers.
//
// Approach (2D DP - matching the existing DP format):
//   - Let total = sum(nums), and target = total / 2.
//   - Build a 2D DP table dp[n+1][target+1] where dp[i][j] indicates whether a subset
//     using the first i elements can achieve sum j.
//   - Base case: dp[i][0] = true for all i (sum 0 is always achievable).
//   - Transition:
//     if nums[i-1] > j:
//     dp[i][j] = dp[i-1][j]
//     else:
//     dp[i][j] = dp[i-1][j] || dp[i-1][j - nums[i-1]]
//   - After filling the table, find the largest j ≤ target such that dp[n][j] is true.
//   - The minimum difference is total - 2*j.
//
// Time complexity: O(n * total_sum)
// Space complexity: O(n * total_sum)
func minSubsetSumDiff(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}

	total := 0
	for _, v := range nums {
		total += v
	}
	target := total / 2

	// dp[i][j] = whether we can achieve sum j using first i elements
	dp := make([][]bool, n+1)
	for i := range dp {
		dp[i] = make([]bool, target+1)
	}

	// Base case: sum 0 is achievable with any number of items (empty subset)
	for i := 0; i <= n; i++ {
		dp[i][0] = true
	}

	// Fill DP table
	for i := 1; i <= n; i++ {
		for j := 1; j <= target; j++ {
			if nums[i-1] > j {
				dp[i][j] = dp[i-1][j]
			} else {
				include := dp[i-1][j-nums[i-1]]
				exclude := dp[i-1][j]
				dp[i][j] = include || exclude
			}
		}
	}

	// Find largest achievable j (≤ target) in the last row
	sum1 := 0
	for j := target; j >= 0; j-- {
		if dp[n][j] {
			sum1 = j
			break
		}
	}

	sum2 := total - sum1
	if sum2 >= sum1 {
		return sum2 - sum1
	}
	return sum1 - sum2
}

// Simple table-driven tests executed in main(), to mirror the lightweight testing in other folders.
func main() {
	tests := []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 6, 11, 5}, 1},
		{[]int{3, 1, 4, 2, 2, 1}, 1},
		{[]int{1, 2, 3, 9}, 3},
		{[]int{10, 20, 15, 5, 25}, 5},
		{[]int{1, 2, 7, 1, 5}, 0},
		{[]int{1, 2, 3, 4, 5, 6, 7}, 0},
		{append(make([]int, 30, 31), 100), 70}, // 30 ones + 100
		{[]int{}, 0},
		{[]int{5}, 5},
		{[]int{1, 1}, 0},
		{[]int{2, 2, 2, 2}, 0},
	}

	// Create 30 ones for the specific test case
	ones := make([]int, 30)
	for i := range ones {
		ones[i] = 1
	}
	tests[6].nums = append(ones, 100)

	for _, tc := range tests {
		got := minSubsetSumDiff(tc.nums)
		fmt.Printf("nums=%v -> got=%d, expected=%d, pass=%v\n", tc.nums, got, tc.expected, got == tc.expected)
	}
}
