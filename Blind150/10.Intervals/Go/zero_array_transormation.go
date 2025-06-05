// https://leetcode.com/problems/zero-array-transformation-i/description/
func isZeroArray(nums []int, queries [][]int) bool {

	n := len(nums)

	diff := make([]int, n+1)

	// create the diff array
	for _, v := range queries {

		l, r := v[0], v[1]
		diff[l]++
		diff[r+1]--
	}

	// create the prefix array
	cur := 0
	prefix := make([]int, n+1)

	for i := 0; i < n; i++ {

		cur = cur + diff[i]

		prefix[i] = cur
	}

	// check if nums[i] > prefix[i]
	for i := 0; i < n; i++ {

		if nums[i] > prefix[i] {
			return false
		}

	}

	return true

}
