// https://leetcode.com/problems/subsets-ii/
func subsetsWithDup(nums []int) [][]int {
	ans := make([][]int, 0)

	sort.Ints(nums)

	var dfs func(idx int, tmp []int)

	dfs = func(idx int, tmp []int) {

		subset := make([]int, len(tmp))
		copy(subset, tmp)
		ans = append(ans, subset)

		for i := idx; i < len(nums); i++ {

			if i > idx && nums[i] == nums[i-1] {
				continue
			}

			tmp = append(tmp, nums[i]) // include the selected number
			dfs(i+1, tmp)
			tmp = tmp[:len(tmp)-1] // bacltrack
		}
	}

	dfs(0, []int{})

	return ans
}
