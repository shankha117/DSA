# https://leetcode.com/problems/decode-string/description/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:

            if c != "]":
                stack.append(c)

            else:
                # find the string to multiply
                substr = ""
                # no need to check if the stack is empty , because we gaurenteed to find
                # an opening bracket once we have found the closing one
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # pop the opening bracket
                stack.pop()

                # find the interger to multiply
                m_str = ""
                while stack and stack[-1].isdigit():
                    m_str = stack.pop() + m_str

                m_number = int(m_str)


                stack.append(m_number * substr)

        return "".join(stack)
