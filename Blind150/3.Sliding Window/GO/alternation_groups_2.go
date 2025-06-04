// https://leetcode.com/problems/alternating-groups-ii/description
func numberOfAlternatingGroups(colors []int, k int) int {

	N := len(colors)

	l := 0

	res := 0

	for r := 1; r < N+(k-1); r++ {

		if colors[r%N] == colors[(r-1)%N] {

			l = r
		}

		if r-l+1 == k {
			res++
			l++

		}

	}

	return res

}
