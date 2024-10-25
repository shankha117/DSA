// https://leetcode.com/problems/search-in-rotated-sorted-array/description/
func search(nums []int, target int) int {

        l, r := 0, len(nums)-1

        for l <= r {

            mid := l + (r - l) /2

            if target == nums[mid]{
                return mid
            }

            // if the mid is in the left side sorted array
            if nums[mid] >= nums[l] {

                if nums[mid] < target || target < nums[l]{
                    l = mid + 1
                }else{
                    r = mid - 1
                }
            }else{
                // mid is in the right side sorted array
                if target < nums[mid] || target > nums[r]{
                    r = mid - 1
                }else{
                    l = mid + 1
                }

            }
        }

        return -1

}
