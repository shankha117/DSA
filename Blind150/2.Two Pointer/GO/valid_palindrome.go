// https://leetcode.com/problems/valid-anagram/

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func isAlnum(r rune) bool {

	return unicode.IsLetter(r) ||unicode.IsDigit(r)
}


func isPalindrome(s string) bool {
	i := 0
	j := len(s)-1
	s = strings.ToLower(s) // this should be `=` not `:=` ; as s will not be a new variable

	for i<j {

		if !isAlnum(rune(s[i])){
			i ++
			continue
		}

		if !isAlnum(rune(s[j])){
			j --
			continue
		}

		if s[i] != s[j]{
			return false
		}

		i++
		j--

	}

	return true
}
