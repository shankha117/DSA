package main

import "fmt"

func knapsackRecursive(wt []int, val []int, W int, n int) int {
	if n == 0 || W == 0 {
		return 0
	}
	if wt[n-1] > W {
		return knapsackRecursive(wt, val, W, n-1)
	}
	include := val[n-1] + knapsackRecursive(wt, val, W-wt[n-1], n-1)
	exclude := knapsackRecursive(wt, val, W, n-1)
	return max(include, exclude)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	weights := []int{1, 3, 4, 5}
	values := []int{1, 4, 5, 7}
	W := 7
	n := len(weights)

	fmt.Println("Recursive:", knapsackRecursive(weights, values, W, n))
}
