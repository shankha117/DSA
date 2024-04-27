
# https://leetcode.com/problems/valid-parentheses/description/

# O(n) solution
class Solution:
    def isValid(self, s: str) -> bool:
        
        paren_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for p in s:
            
            # if p is a closing bracket
            if p in paren_map:
                
                # check if the top of the satck has matchig opening bracket
                if stack and stack[-1] == paren_map[p]:

                    stack.pop()
                
                else:
                    return False
            # if p is a opening bracket push it to the stack 

            else:

                stack.append(p)

        return stack == []
    

if __name__ == "__main__":
    
    s1 = "({}{}[])"
    s2 = "([[]{}][])"
    s3 = "())))"
    s4 = "({{{{][}}}})"


    c  = Solution()

    print(f" is {s1} a valid parenthesisis string -->  {c.isValid(s1)} \n")
    print(f" is {s2} a valid parenthesisis string -->  {c.isValid(s2)} \n")
    print(f" is {s3} a valid parenthesisis string -->  {c.isValid(s3)} \n")
    print(f" is {s4} a valid parenthesisis string -->  {c.isValid(s4)} \n")

