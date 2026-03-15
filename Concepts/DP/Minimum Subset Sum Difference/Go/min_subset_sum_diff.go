package main

import (
	"fmt"
	"math"
)

// MinSubsetSumDifference computes the minimum possible difference between the sums
// of two subsets partitioned from the input array of positive integers.
// Approach:
//   - Let total be the sum of all elements.
//   - If we can achieve some subset sum s (0 <= s <= total/2), the other subset is total - s,
//     and the difference is total - 2*s.
//   - We therefore want the achievable s closest to total/2.
//   - Use 0/1 subset-sum DP to compute achievable sums up to total/2.
//
// Time complexity: O(n * totalSum)
// Space complexity: O(totalSum)
func MinSubsetSumDifference(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	total := 0
	for _, v := range nums {
		total += v
	}
	target := total / 2

	// dp[s] indicates whether sum s is achievable.
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
	// Fallback; theoretically unreachable since dp[0] is always true.
	return 0
}

// MinSubsetSumDifferenceBitset is an alternative bitset-based implementation.
// It can be faster in practice due to bit operations.
// Note: For very large sums, shifting may overflow the integer width.
// This implementation uses Go's built-in uint64 bit operations, so it is suitable
// when the total sum is less than 64 bits wide. For larger sums, prefer the boolean DP.
func MinSubsetSumDifferenceBitset(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	total := 0
	for _, v := range nums {
		total += v
	}
	target := total / 2

	// Use a dynamic bitset via []uint64 to avoid uint64 overflow for large sums.
	// Each bit represents an achievable sum. We need total+1 bits.
	words := (total + 64) / 64
	bitset := make([]uint64, words)
	// sum 0 achievable
	bitset[0] = 1

	shiftLeft := func(bs []uint64, shift int) []uint64 {
		if shift == 0 {
			// No shift needed
			out := make([]uint64, len(bs))
			copy(out, bs)
			return out
		}
		wordShift := shift / 64
		bitShift := shift % 64
		out := make([]uint64, len(bs))
		for i := len(bs) - 1; i >= 0; i-- {
			j := i - wordShift
			if j < 0 {
				continue
			}
			var val uint64 = bs[j] << bitShift
			if bitShift != 0 && j-1 >= 0 {
				val |= bs[j-1] >> (64 - bitShift)
			}
			out[i] = val
		}
		return out
	}

	orInPlace := func(a, b []uint64) {
		for i := range a {
			a[i] |= b[i]
		}
	}

	for _, num := range nums {
		shifted := shiftLeft(bitset, num)
		orInPlace(bitset, shifted)
	}

	// Find achievable s <= target closest to target
	for s := target; s >= 0; s-- {
		wordIdx := s / 64
		bitIdx := uint(s % 64)
		if (bitset[wordIdx]>>bitIdx)&1 == 1 {
			return total - 2*s
		}
	}
	return 0
}

func main() {
	tests := []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 2, 3, 9}, 3},
		{[]int{1, 2, 7}, 4},
		{[]int{3, 1, 4, 2, 2, 1}, 1},
		{[]int{}, 0},
		{[]int{5}, 5},
		{[]int{1, 1, 1, 1}, 0},
		{[]int{2, 2, 2, 2, 2}, 0},
		{[]int{1, 6, 11, 5}, 1}, // classic example
	}

	for _, tc := range tests {
		res := MinSubsetSumDifference(tc.nums)
		resBit := MinSubsetSumDifferenceBitset(tc.nums)
		fmt.Printf("nums=%v, dp=%d, bitset=%d, expected=%d, ok=%v\n",
			tc.nums, res, resBit, tc.expected, res == tc.expected && resBit == tc.expected)
	}

	// Example: large sums may be better with boolean DP due to bitset memory cost.
	large := make([]int, 100)
	for i := range large {
		large[i] = 1
	}
	fmt.Printf("large dp=%d\n", MinSubsetSumDifference(large))

	// Sanity: small random-like case
	nums := []int{7, 3, 2, 5, 8}
	fmt.Printf("nums=%v -> min diff=%d (dp), %d (bitset)\n",
		nums, MinSubsetSumDifference(nums), MinSubsetSumDifferenceBitset(nums))

	// Edge: single element
	fmt.Println("single [10] ->", MinSubsetSumDifference([]int{10}))

	// Edge: two elements
	fmt.Println("two [10, 10] ->", MinSubsetSumDifference([]int{10, 10}))

	// Edge: varying values
	fmt.Println("mixed [10, 20, 15, 5] ->", MinSubsetSumDifference([]int{10, 20, 15, 5}))

	// Demonstrate difference formula correctness:
	// If closest s to total/2 is found, difference is total - 2*s.
	fmt.Println("formula check [1,2,3,9]: total=15, closest s≈7 -> diff=15-2*7=1? Actually achievable s=6 -> diff=15-12=3")
}

// Optional helper to compute absolute difference directly from partition sums.
// Not used in the DP, but shows relationship with total - 2*s.
func absDiff(a, b int) int {
	return int(math.Abs(float64(a - b)))
}
