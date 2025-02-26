package main

import (
	"fmt"
)

// computeLPS computes the Longest Prefix Suffix (LPS) array.
func computeLPS(pattern string) []int {
	lps := make([]int, len(pattern))
	length := 0 // Length of the previous longest prefix suffix
	i := 1

	for i < len(pattern) {
		if pattern[i] == pattern[length] {
			length++
			lps[i] = length
			i++
		} else {
			if length != 0 {
				length = lps[length-1] // Reduce length and retry
			} else {
				lps[i] = 0
				i++
			}
		}
	}
	return lps
}

// kmpSearch searches for occurrences of pattern in text using KMP algorithm.
func kmpSearch(text, pattern string) []int {
	if len(pattern) == 0 {
		return []int{}
	}

	lps := computeLPS(pattern)
	i, j := 0, 0 // i -> index for text, j -> index for pattern
	var result []int

	for i < len(text) {
		if text[i] == pattern[j] {
			i++
			j++
			if j == len(pattern) { // Found a match
				result = append(result, i-j)
				j = lps[j-1] // Use LPS to continue searching
			}
		} else if j > 0 {
			j = lps[j-1] // Use LPS to skip unnecessary comparisons
		} else {
			i++ // Move to the next character in text
		}
	}
	return result
}

func main() {
	text := "ababcababcabc"
	pattern := "abc"
	fmt.Println(kmpSearch(text, pattern)) // Output: [2 7 10]
}
