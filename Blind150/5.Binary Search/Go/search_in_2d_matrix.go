
// https://leetcode.com/problems/search-a-2d-matrix/description/
func searchMatrix(matrix [][]int, target int) bool {

    rows, cols := len(matrix), len(matrix[0])
    t,b := 0, rows - 1
    row := -1

    for t <= b{

        mid := t + (b -t) / 2

        if target > matrix[mid][cols - 1] {
            t = mid + 1
        }else if target < matrix[mid][0] {
            b = mid - 1
        }else{
            row = mid
            break
        }
    }

    if row == -1 {
        return false
    }

    l,r := 0, cols - 1

    for l <= r {
        rowMid := l + ( r-l) / 2

        if matrix[row][rowMid] == target{
            return true
        }else if target >  matrix[row][rowMid]{
            l = rowMid + 1
        }else{
            r = rowMid - 1
        }
    }
    return false

}
