// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

func twoSum(numbers []int, target int) []int {

    l, r := 0, len(numbers) -1

    for l < r {

        curSum := numbers[l] + numbers[r]

        if curSum > target{

            r = r - 1
        }else if curSum < target{

            l = l + 1
        }else{

            return []int{l+1, r+1}
        }

    }

    return []int{l+1, r+1}

}
