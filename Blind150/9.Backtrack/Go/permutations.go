// https://leetcode.com/problems/permutations/description/
func permute(nums []int) [][]int {

	ans := make([][]int, 0)

	seen := make(map[int]bool)

	N := len(nums)

	var dfs func(tmp []int, seen map[int]bool)

	dfs = func(tmp []int, seen map[int]bool) {

		if len(tmp) == N {
			subset := make([]int, N)

			copy(subset, tmp)

			ans = append(ans, subset)

			return
		}

		for _, num := range nums {

			if !seen[num] {

				tmp = append(tmp, num)
				seen[num] = true

				dfs(tmp, seen)

				tmp = tmp[:len(tmp)-1]
				delete(seen, num)
			}

		}

	}

	dfs([]int{}, seen)

	return ans

}
