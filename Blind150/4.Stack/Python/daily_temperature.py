# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []

        output = [0]*len(temperatures)

        for pos, val in enumerate(temperatures):

            while st and val > st[-1][0]:

                cur_t_val, cur_t_idx = st.pop()
                output[cur_t_idx] = pos - cur_t_idx

            st.append((val, pos))

        return output
