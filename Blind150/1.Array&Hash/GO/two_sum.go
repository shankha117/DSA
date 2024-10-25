// https://leetcode.com/problems/two-sum/description/

package main

import "fmt"

func twoSum(nums []int, target int) []int {

	seenDict := make(map[int]int)

	for pos, val := range nums {

		if found, ok := seenDict[target-val]; ok {

			return []int{found, pos}
		}

		seenDict[val] = pos

	}

	return []int{}

}

func main() {

	SumArray := []int{2, 7, 11, 15}

	ans := twoSum(SumArray, 9)

	fmt.Printf("Ans is %v \n ", ans)

}
