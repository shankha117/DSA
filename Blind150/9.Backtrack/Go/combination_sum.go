// https: //leetcode.com/problems/combination-sum/description/
func combinationSum(candidates []int, target int) [][]int {

	ans := make([][]int, 0)

	var dfs func(idx int, s int, tmp []int)

	dfs = func(idx int, s int, tmp []int) {

		if s == target {

			subset := make([]int, len(tmp))
			copy(subset, tmp)
			ans = append(ans, subset)

		}

		if s > target {
			return
		}

		for i := idx; i < len(candidates); i++ {

			tmp = append(tmp, candidates[i])

			dfs(i, s+candidates[i], tmp)

			tmp = tmp[:len(tmp)-1]

		}

	}

	dfs(0, 0, []int{})

	return ans

}
