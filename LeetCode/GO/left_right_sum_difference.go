// https://leetcode.com/problems/left-and-right-sum-differences/description/

package main

import "fmt"

func leftRightDifference(nums []int) []int {
	lSum, rSum := 0, 0
	n := len(nums)
	answer := make([]int, n)

	for _, val := range nums {
		rSum += val
	}

	for pos, val := range nums {

		if pos > 0 {
			lSum += nums[pos-1]
		}
		rSum -= val

		answer[pos] = abs(lSum - rSum)
	}
	return answer
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {

	nums1 := []int{10, 4, 8, 3}
	nums2 := []int{1}

	fmt.Printf("The ans for %v is %v \n", nums1, leftRightDifference(nums1))
	fmt.Printf("The ans for %v is %v \n", nums2, leftRightDifference(nums2))

}
