package main

import (
	"fmt"
	"strconv"
)

type Solution struct{}

func (s *Solution) Encode(strs []string) string {

	res := ""

	for _, s := range strs {

		res += strconv.Itoa(len(s)) + "C" + s
	}

	return res

}

func (s *Solution) Decode(encoded string) []string {

	res := make([]string, 0)

	i := 0

	for i < len(encoded) {

		j := i

		for string(encoded[j]) != "C" {

			j++
		}

		count, _ := strconv.Atoi(encoded[i:j])

		res = append(res, encoded[j+1:j+1+count])

		i = j + 1 + count

	}
	return res

}
func main() {
	solution := Solution{}

	// Example usage:
	originalStrings := []string{"hello", "world", "golang"}
	encoded := solution.Encode(originalStrings)
	fmt.Println("Encoded:", encoded)

	decoded := solution.Decode(encoded)
	fmt.Println("Decoded:", decoded)
}

// output
// Encoded: 5Chello5Cworld6Cgolang
// Decoded: [hello world golang]
