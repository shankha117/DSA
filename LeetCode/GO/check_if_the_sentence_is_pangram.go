// https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func checkIfPangram(sentence string) bool {
	if len(sentence) < 26 {
		return false
	}

	// Initialize the map with all lowercase letters
	alphaDict := make(map[rune]int)
	for ch := 'a'; ch <= 'z'; ch++ {
		alphaDict[ch] = 0
	}

	// Iterate over the sentence and update the map
	for _, ch := range sentence {
		if unicode.IsLower(ch) {
			alphaDict[ch] = 1
		}
	}

	// Count the number of unique lowercase letters
	count := 0
	for _, v := range alphaDict {
		count += v
	}

	// Check if the count equals 26
	return count == 26

}

// This COULD BE A BETTER AND CLEANER SOLUTION
func checkIfPangram2(sentance string) {
	for chars := 97; chars < 123; chars++ {

		// check if all the alphabates are in the string

		if strings.Index(sentence, string(chars)) < 0 {
			return false
		}
	}
	return true
}

func main() {

	src_sentence1 := "thequickbrownfoxjumpsoverthelazydog"
	src_sentence2 := "shankha"

	fmt.Printf("\n is the sentance %v panagram ? %v \n\n", src_sentence1, checkIfPangram(src_sentence1))
	fmt.Printf("\n is the sentance %v panagram ? %v \n\n", src_sentence2, checkIfPangram(src_sentence2))

}
