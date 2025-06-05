package main

import "fmt"

func knapsackMemo(wt []int, val []int, W int, n int) int {
	// Create a 2D slice initialized to -1
	memo := make([][]int, n+1)
	for i := range memo {
		memo[i] = make([]int, W+1)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}

	var solve func(n, W int) int
	solve = func(n, W int) int {
		if n == 0 || W == 0 {
			return 0
		}
		if memo[n][W] != -1 {
			return memo[n][W]
		}
		if wt[n-1] > W {
			memo[n][W] = solve(n-1, W)
		} else {
			include := val[n-1] + solve(n-1, W-wt[n-1])
			exclude := solve(n-1, W)
			memo[n][W] = max(include, exclude)
		}
		return memo[n][W]
	}

	return solve(n, W)
}

func main() {
	weights := []int{1, 3, 4, 5}
	values := []int{1, 4, 5, 7}
	W := 7
	n := len(weights)

	fmt.Println("Memoization:", knapsackMemo(weights, values, W, n))
}
