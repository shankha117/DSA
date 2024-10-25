// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// Helper function to return the maximum of two integers
func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func lengthOfLongestSubstring(s string) int {

    if len(s) == 1 || len(s) == 0 {
        return len(s)
    }
    l := 0
    seenMap := make(map[byte]int)
    seenMap[s[l]] = 0
    maxLength := 1

    for r:=1 ; r<len(s) ; r++ {
        if index, found := seenMap[s[r]] ; found {
            l = max(index + 1, l)
        }
        seenMap[s[r]] = r
        maxLength = max(maxLength, (r-l)+1)
    }
    return maxLength

}
