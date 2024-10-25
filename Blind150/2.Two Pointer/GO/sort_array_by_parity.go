// https://leetcode.com/problems/sort-array-by-parity/description/

// Solution1
func sortArrayByParity(nums []int) []int {

    l, r := 0, len(nums)-1

    for l <= r {
        if nums[l] % 2 != 0 {
            nums[l], nums[r] = nums[r], nums[l]
            r --
        }else{
            l ++
        }
    }
    return nums
}

// Solution2
func sortArrayByParity2(nums []int) []int {

    p := 0

    for i:=0 ; i < len(nums) ; i++ {

        if nums[i] %2 == 0 {
            nums[i], nums[p] = nums[p], nums[i]
            p ++
        }
    }
    return nums
}
