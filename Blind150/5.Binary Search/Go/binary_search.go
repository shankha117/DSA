// https://leetcode.com/problems/binary-search/description/

func search(nums []int, target int) int {

    low, high := 0, len(nums) - 1

    for low <= high {

        mid := low + (high-low)/2

        if nums[mid] == target {

            return mid

        }else if nums[mid] < target {

            low = mid + 1

        }else{

            high = mid - 1
        }

    }

    return -1

}
