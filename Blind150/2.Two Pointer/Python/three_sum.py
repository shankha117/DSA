# https://leetcode.com/problems/3sum/description/
#
class Solution:

    def twoSum(self, l,r, nums , target):

        ans = []

        while l < r:

            cur_sum = nums[l] + nums[r]
            if  cur_sum > target:

                r -= 1

            elif cur_sum < target:

                l += 1

            else:
                ans.append([nums[l],nums[r]])

                l += 1

                # dry run this [-2,0,0,2,2]
                while nums[l] == nums[l-1] and l < r:
                    l += 1


        return ans


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()


        for pos, val in enumerate(nums):

            if pos > 0 and nums[pos] == nums[pos-1]:
                continue

            l,r = pos+1, len(nums)-1

            found = self.twoSum(l,r,nums,0-val)

            for r in found:
                res.append([val]+ r)

        return res
