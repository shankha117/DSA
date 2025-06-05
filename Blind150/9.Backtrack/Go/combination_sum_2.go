// https://leetcode.com/problems/combination-sum-ii/
func combinationSum2(candidates []int, target int) [][]int {

	ans := make([][]int, 0)

	N := len(candidates)

	sort.Ints(candidates)

	var dfs func(idx int, tot int, tmp []int)

	dfs = func(idx int, tot int, tmp []int) {

		if tot == target {

			subset := make([]int, len(tmp))
			copy(subset, tmp)
			ans = append(ans, subset)
			return
		}

		for i := idx; i < N; i++ {

			if i > idx && candidates[i] == candidates[i-1] {
				continue
			}

			if candidates[i] > target || tot+candidates[i] > target {
				break
			}

			tmp = append(tmp, candidates[i])

			dfs(i+1, tot+candidates[i], tmp)

			tmp = tmp[:len(tmp)-1]

		}

	}

	dfs(0, 0, []int{})

	return ans

}
