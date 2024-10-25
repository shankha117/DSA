package main

import (
	"fmt"
)

func isValid(s string) bool {

	paren_map := map[rune]rune{')': '(', '}': '{', ']': '['}
	stack := []rune{}

	for _, p := range s {

		if val, ok := paren_map[p]; ok {

			if len(stack) > 0 && stack[len(stack)-1] == val {

				stack = stack[:len(stack)-1]
			} else {

				return false
			}
		} else {
			// If p is an opening bracket, push it to the stack
			stack = append(stack, p)
		}

	}

	return len(stack) == 0

}

func main() {

	s1 := "({}{}[])"
	s2 := "([[]{}][])"
	s3 := "())))"
	s4 := "({{{{][}}}})"

	fmt.Printf("is %s a valid parenthesis --->>> %v\n", s1, isValid(s1))
	fmt.Printf("is %s a valid parenthesis --->>> %v\n", s2, isValid(s2))
	fmt.Printf("is %s a valid parenthesis --->>> %v\n", s3, isValid(s3))
	fmt.Printf("is %s a valid parenthesis --->>> %v\n", s4, isValid(s4))

}
