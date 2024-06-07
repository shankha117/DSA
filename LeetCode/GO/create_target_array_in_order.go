// https://leetcode.com/problems/create-target-array-in-the-given-order/description/

package main

import (
	"fmt"
	"slices"
)

func createTargetArray(nums []int, index []int) []int {

	ans := make([]int, 0)
	for i, v := range nums {
		ans = slices.Insert(ans, index[i], v)
	}
	return ans

}

/*
how does ths slicing works
>>> x = [1,2,4,5]
>>> x[1:1]
[]
>>> x[1:]
[2, 4, 5]
>>> x[1:1] = [1]
>>> x
[1, 1, 2, 4, 5]
>>> x[1:1] = [2,3]
>>> x
[1, 2, 3, 1, 2, 4, 5]
>>> x[1:4] = [1]
>>> x
[1, 1, 2, 4, 5]
>>> x[0:2] = [1]
>>> x
[1, 2, 4, 5]
>>>
*/

func main() {

	nums1 := []int{0, 1, 2, 3, 4}
	index1 := []int{0, 1, 2, 2, 1}

	// ans [0,4,1,3,2]

	fmt.Printf("\n The ans for %v is %v \n\n", nums1, createTargetArray(nums1, index1))

}
