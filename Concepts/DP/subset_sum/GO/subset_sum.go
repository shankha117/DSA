package main

import "fmt"

func SubsetSum(nums []int, target int) bool {

	n := len(nums)
	dp := make([][]bool, n+1)

	for i := range dp {
		dp[i] = make([]bool, target+1)
		dp[i][0] = true
	}

	for i := 1; i < n+1; i++ {
		for j := 1; j < target+1; j++ {

			if nums[i-1] <= j {
				include := dp[i-1][j-nums[i-1]]
				exclude := dp[i-1][j]
				dp[i][j] = include || exclude
			} else {
				dp[i][j] = dp[i-1][j]
			}

		}
	}

	return dp[n][target]

}

func main() {
	tests := []struct {
		nums   []int
		target int
		want   bool
	}{
		{[]int{3, 34, 4, 12, 5, 2}, 9, true},         // Medium
		{[]int{3, 34, 4, 12, 5, 2}, 30, false},       // Medium (impossible)
		{[]int{1, 2, 3, 4, 5}, 10, true},             // Medium
		{[]int{1, 2, 7, 1, 5}, 9, true},              // Medium
		{[]int{1, 3, 5, 7}, 12, true},                // Medium
		{[]int{2, 3, 7, 8, 10}, 11, true},            // Hard
		{[]int{2, 3, 7, 8, 10}, 14, false},           // Hard
		{[]int{2, 3, 7, 8, 10}, 27, true},            // Hard (not possible)
		{[]int{100, 200, 300, 400, 500}, 1500, true}, // Hard (sum all)
		{[]int{100, 200, 300, 400, 500}, 50, false},  // Hard (too small)
	}

	for i, tt := range tests {
		got := SubsetSum(tt.nums, tt.target)
		if got != tt.want {
			fmt.Printf("Test %d FAILED: SubsetSum(%v, %d) = %v; want %v\n", i+1, tt.nums, tt.target, got, tt.want)
		} else {
			fmt.Printf("Test %d passed.\n", i+1)
		}
	}
}
