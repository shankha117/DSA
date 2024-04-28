package main

import "fmt"

// https://leetcode.com/problems/number-of-good-pairs/

func numIdenticalPairs(nums []int) int {

	if len(nums) == 0 {
		return 0
	}

	seenDict := make(map[int][]int)

	ans := 0

	for pos, val := range nums {

		if valList, ok := seenDict[val]; ok {
			ans += len(valList)
		}

		seenDict[val] = append(seenDict[val], pos)
	}

	return ans

}

func main() {

	nums := []int{1, 2, 3, 1, 1, 3}

	fmt.Printf("THe number of good pairs are %v ", numIdenticalPairs(nums))

}
