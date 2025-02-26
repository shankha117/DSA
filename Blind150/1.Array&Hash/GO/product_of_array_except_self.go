// https://leetcode.com/problems/product-of-array-except-self/description/
func productExceptSelf(nums []int) []int {

	res := make([]int, len(nums)) // Create a slice with length equal to len(nums)

	res[0] = 1
	prefix := 1

	for i := 0; i < len(nums); i++ {

		res[i] = prefix
		prefix *= nums[i]

	}

	postfix := 1

	for i := len(nums) - 1; i >= 0; i-- {

		res[i] = res[i] * postfix

		postfix = postfix * nums[i]
	}

	return res
}
