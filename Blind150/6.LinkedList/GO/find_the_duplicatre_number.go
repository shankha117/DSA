// https://leetcode.com/problems/find-the-duplicate-number/description/
func findDuplicate(nums []int) int {

	slow, fast := 0, 0

	for {

		slow = nums[slow]
		fast = nums[nums[fast]]

		if slow == fast {

			fast = 0

			for fast != slow {
				fast = nums[fast]
				slow = nums[slow]

			}

			break

		}

	}

	return slow

}
