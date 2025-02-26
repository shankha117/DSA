package main

import "fmt"

// https://leetcode.com/problems/number-of-good-pairs/

// I dont event have to keep track of the positions .... Just remember how many times that occured
func numIdenticalPairs2(nums []int) int {
	count := make(map[int]int)
	result := 0

	for _, num := range nums {
		if _, exists := count[num]; exists {
			result += count[num]
			count[num]++
		} else {
			count[num] = 1
		}
	}

	return result
}

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

	fmt.Printf("THe number of good pairs are %v \n", numIdenticalPairs(nums))

	fmt.Printf("THe number of good pairs are %v ", numIdenticalPairs2(nums))

}
