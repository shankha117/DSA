// https://leetcode.com/problems/permutation-in-string/description/
func checkInclusion(s1 string, s2 string) bool {

	l1, l2 := len(s1), len(s2)

	if l2 < l1 {
		return false
	}

	var countl1, countl2 [26]int

	for _, ch := range s1 {
		// fmt.Println(ch, ch - 'a')
		countl1[ch-'a']++
	}

	for i := 0; i < l1; i++ {
		countl2[s2[i]-'a']++
	}

	if countl1 == countl2 {
		return true
	}

	for i := 0; i < (l2 - l1); i++ {

		countl2[s2[i]-'a']--

		countl2[s2[i+l1]-'a']++

		if countl2 == countl1 {
			return true
		}
	}

	return false

}
