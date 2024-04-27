from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]

        strs.sort(key=len)

        res = ""

        for i in range(len(strs[0])):

            for s in strs[1:]:

                if s[i] != strs[0][i]:
                    
                    return res
            
            res += strs[0][i]

        return res
    


if __name__ == "__main__":
    
    strs1 = ["flower","flow","flight"]
    
    s  = Solution()
    
    print(f" LCP op {strs1} is {s.longestCommonPrefix(strs1)}")
