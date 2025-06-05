import (
	"fmt"
)

func topKFrequent(nums []int, k int) []int {

	fMap := make(map[int]int)

	for _, ele := range nums {

		fMap[ele]++

	}

	// Step 2: Create a slice of slices to store elements by their frequency
	freq := make([][]int, len(nums)+1)

	for key, val := range fMap {

		freq[val] = append(freq[val], key)

	}

	// Step 3: Create an empty result slice
	res := []int{}

	fmt.Println(freq)

	for i := len(freq) - 1; i > 0; i-- {

		for _, n := range freq[i] {

			res = append(res, n)

			if len(res) == k {

				return res
			}

		}

	}

	return res

}
