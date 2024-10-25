// https://leetcode.com/problems/valid-anagram/description/


// Why Use rune(s[i]) in the isAnagram Example?
// Unicode Characters: If the string contains non-ASCII characters (e.g., characters with accents, Chinese characters), they may consist of multiple bytes. s[i] would only give you one byte, which might not represent a complete character. rune(s[i]) ensures you're dealing with the full Unicode code point.
// Consistency: By using rune(s[i]), you're ensuring that your code correctly handles all characters, not just single-byte ASCII characters.


package main

import (
	"fmt"
)

func isAnagram(s, t string) bool {

	if len(s) != len(t){
		return false
	}

	countS := make(map[rune]int)
	countT := make(map[rune]int)

	for i:=0 ; i<len(s); i++ {

		countS[rune(s[i])] ++
		countT[rune(t[i])] ++

	}

	for key, val := range countS{
		if countT[key] != val{
			return false
		}
	}


	return true
}
