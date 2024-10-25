// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
func findMin(nums []int) int {

        // if the. array is already sorted return 0
        if nums[0] < nums[len(nums)-1]{
            return nums[0]
        }
    	// Initialize result with the first element
        res := nums[0]
        l, r := 0, len(nums)-1

        for l <= r {
            // If the array is already sorted, return the minimum of res and nums[l]
            if nums[l] < nums[r] {
                return min(res, nums[l])
            }

            // Calculate the middle index
            m := (l + r) / 2

            // Update the result with the minimum value at mid
            res = min(res, nums[m])

            // If the middle element is greater than or equal to the left element,
            // it means the minimum is on the right side
            if nums[m] >= nums[l] {
                l = m + 1
            } else {
                // Otherwise, the minimum is on the left side
                r = m - 1
            }
        }
        return res
}
