package main

import "fmt"

func romanToInt(s string) int {

	res := 0

	roman := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	for i := 0; i < len(s); i++ {

		if i+1 < len(s) && roman[s[i]] < roman[s[i+1]] {

			res -= roman[s[i]]

		} else {
			res += roman[s[i]]
		}
	}

	return res

}

func main() {

	s1, s2, s3 := "CMXCVIII", "LVIII", "MCMXCIV"

	fmt.Printf(" INTEGER OF %v is %v \n", s1, romanToInt(s1))
	fmt.Printf(" INTEGER OF %v is %v \n", s2, romanToInt(s2))
	fmt.Printf(" INTEGER OF %v is %v \n", s3, romanToInt(s3))

}
