// https://leetcode.com/problems/group-anagrams/


import (
	"sort"
)


func sortStrings(ele string) string {
	r := []rune(ele)

	sort.Slice(r, func(i,j int) bool { return r[i] < r[j] })

	return string(r)
}


func groupAnagrams(strs []string) [][]string {

	tmp := make(map[string][]string)


	for _, ele := range strs {

		sorted_str := sortStrings(ele)

		tmp[sorted_str] = append(tmp[sorted_str], ele)

	}

	ans := make([][]string,0)


	for _, val := range tmp {

		ans = append(ans, val)
	}

	return ans




}
