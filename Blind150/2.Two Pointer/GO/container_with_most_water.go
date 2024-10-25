// https://leetcode.com/problems/container-with-most-water/description/

func maxArea(height []int) int {

    l,r := 0, len(height) - 1

    maxArea := 0

    for l < r {

        curArea := (r-l)*min(height[l], height[r])

        maxArea = max(maxArea, curArea)

        if height[l] < height[r] {

            l = l + 1
        }else{
            r = r - 1
        }
    }
    return maxArea
}
