// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
func canBeSwapped(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	if s1 == s2 {
		return true
	}

	setS1 := make(map[byte]struct{})
	setS2 := make(map[byte]struct{})
	notMatched := 0

	for i := 0; i < len(s1); i++ {
		x := s1[i]
		y := s2[i]

		if x != y {
			setS1[x] = struct{}{}
			setS2[y] = struct{}{}

			notMatched++

			if notMatched > 2 {
				return false
			}
		}
	}

	if len(setS1) != len(setS2) {
		return false
	}

	for key := range setS1 {
		if _, exists := setS2[key]; !exists {
			return false
		}
	}

	return true
}
