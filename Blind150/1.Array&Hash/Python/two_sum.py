from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        seen_dict = {}

        for pos, val in enumerate(nums):

            if target-val in seen_dict:

                return [seen_dict[target-val], pos]
            
            seen_dict[val] = pos


if __name__ == "__main__":
    
    nums = [2,7,11,15] 
    target = 9

    c  = Solution().twoSum(nums=nums, target=target)

    print(f" The solution is {c} \n")

