// https://leetcode.com/problems/decode-string/description/
func decodeString(s string) string {

	var stack []string

	for _, c := range s {

		char := string(c)

		if char != "]" {

			stack = append(stack, char)
		} else {
			// Find the string to multiply
			substr := ""
			// no need to check if the stack is empty , because we gaurenteed to find
			// an opening bracket once we have found the closing one

			for stack[len(stack)-1] != "[" {

				substr = stack[len(stack)-1] + substr

				stack = stack[:len(stack)-1]
			}

			// pop the opening bracket
			stack = stack[:len(stack)-1]

			// Find the integer to multiply
			mStr := ""

			for len(stack) > 0 && isDigit(stack[len(stack)-1]) {

				mStr = stack[len(stack)-1] + mStr

				stack = stack[:len(stack)-1]

			}

			mNum, _ := strconv.Atoi(mStr)

			stack = append(stack, strings.Repeat(substr, mNum))

		}

	}

	return strings.Join(stack, "")
}

func isDigit(s string) bool {
	_, err := strconv.Atoi(s)
	return err == nil
}
