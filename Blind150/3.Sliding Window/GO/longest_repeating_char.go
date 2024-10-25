// https://leetcode.com/problems/longest-repeating-character-replacement/description/

func characterReplacement(s string, k int) int {

    countMap := make(map[byte]int)
    res := 1
    l , r, maxF := 0,1, 1
    countMap[s[l]] = 1

    for r < len(s) {

        countMap[s[r]] ++
        maxF = max(maxF, countMap[s[r]])
        curLen := (r-l) + 1

        if curLen - maxF <= k {
            res = max(res, curLen)
            r ++
        }else{

            countMap[s[r]] --
            countMap[s[l]] --
            l++
        }
    }
    return res
}
