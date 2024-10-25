// https://leetcode.com/problems/daily-temperatures/description/
func dailyTemperatures(temperatures []int) []int {

    st := [][]int{}

    output := make([]int, len(temperatures))

    for pos, val := range(temperatures) {

        for len(st) > 0 && val > st[len(st)-1][0] {

            curTIdx := st[len(st)-1][1]
            st = st[:len(st)-1]
            output[curTIdx] = pos - curTIdx

        }

        st = append(st, []int{val, pos})
    }

    return output

}
