// https://leetcode.com/problems/3sum/description/


import "sort"

func twoSum(l int,r int, nums []int, target int) [][]int {

    ans := [][]int{}
    for l < r {

        cur_sum := nums[l] + nums[r]

        if  cur_sum > target{

            r = r - 1
        }else if cur_sum < target{

            l = l + 1
        }else{

            ans  = append(ans, []int{nums[l],nums[r]})

            l = l + 1

            for nums[l] == nums[l-1] && l < r {

                l = l + 1
            }
        }
    }
    return ans
}

func threeSum(nums []int) [][]int {


        res := [][]int{}
        // To sort an integer slice:
        sort.Ints(nums)

        for pos, val := range nums{

            if pos > 0 && nums[pos] == nums[pos-1]{
                continue
            }
            l,r := pos+1, len(nums)-1

            found := twoSum(l,r,nums,0-val)

            for _, r := range found{

                // Create a new slice with val and append r
                res = append(res, append([]int{val}, r...))

            }
        }
        return res
}
