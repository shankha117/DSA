package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	s := strconv.Itoa(x)
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true

}

func main() {

	t1, t2, t3 := 1234, -1234, 12321

	fmt.Printf(" is %v is a palindrome number -->> %v \n", t1, isPalindrome(t1))
	fmt.Printf(" is %v is a palindrome number -->> %v \n", t2, isPalindrome(t2))
	fmt.Printf(" is %v is a palindrome number -->> %v \n", t3, isPalindrome(t3))

}
