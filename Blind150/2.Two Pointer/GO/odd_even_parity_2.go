func sortArrayByParityII(nums []int) []int {

    e,o := 0,  1

    for e < len(nums)-1{

        for nums[e] % 2 != 0  && o < len(nums) {

            nums[e], nums[o] = nums[o], nums[e]
            o = o + 2

        }

        e = e + 2


    }

    return nums

}
