package main

import (
	"fmt"
	"sort"
)

func longestCommonPrefix(strs []string) string {

	if len(strs) == 1 {
		return strs[0]
	}

	// sort by length , the smalest one is at the front
	sort.Slice(strs, func(i, j int) bool {
		return len(strs[i]) < len(strs[j])
	})

	res := ""

	for i := range strs[0] {

		for _, s := range strs[1:] {

			if s[i] != strs[0][i] {

				return res

			}

		}

		res += string(strs[0][i])

	}

	return res

}

func main() {

	strs1 := []string{"flower", "flow", "fleet"}
	strs2 := []string{"cat", "car", "cane"}
	strs3 := []string{"arkbcdd", "arlmkbcdd", "arkffcbd"}

	fmt.Printf(" THe larget common prefix for %v is %v \n", strs1, longestCommonPrefix(strs1))
	fmt.Printf(" THe larget common prefix for %v is %v \n", strs2, longestCommonPrefix(strs2))
	fmt.Printf(" THe larget common prefix for %v is %v \n", strs3, longestCommonPrefix(strs3))

}
