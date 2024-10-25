// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

// Solution 1
import (
	"fmt"
	"strconv"
)

// Function to evaluate based on the operator and operands
func evaluate(od1, od2 int, opr string) int {
	switch opr {
	case "+":
		return od1 + od2
	case "-":
		return od1 - od2
	case "*":
		return od1 * od2
	case "/":
		return od1 / od2
	}
	return 0
}

// Function to evaluate Reverse Polish Notation (RPN)
func evalRPN(tokens []string) int {
	oprs := []string{"+", "-", "/", "*"}
	var st []int

	// Helper function to check if a string is an operator
	isOperator := func(t string) bool {
		for _, opr := range oprs {
			if t == opr {
				return true
			}
		}
		return false
	}

	// Iterate through each token in the RPN expression
	for _, t := range tokens {
		if !isOperator(t) {
			// Convert the string token to an integer and push onto the stack
			val, _ := strconv.Atoi(t)
			st = append(st, val)
		} else {
			// Pop the last two elements from the stack (operands)
			od2 := st[len(st)-1]
			od1 := st[len(st)-2]
			st = st[:len(st)-2]

			// Evaluate the result and push it back to the stack
			ans := evaluate(od1, od2, t)
			st = append(st, ans)
		}
	}

	// Return the final result (the only remaining element in the stack)
	return st[0]
}







// Solution 2


type Stack struct{
    stack []int
}


func evalRPN2(tokens []string) int {

    var s Stack

    for _,v := range tokens{

        switch(v){
            case "+":
                s.push(s.pop() + s.pop())
            case "-":
                right := s.pop()
                left := s.pop()
                s.push(left - right)
            case "*":
                s.push(s.pop() * s.pop())
            case "/":
                right := s.pop()
                left := s.pop()
                s.push(left / right)
            default:
                value,_ := strconv.Atoi(v)
                s.push(value)
        }
    }

    return s.pop()


}

func (s *Stack)push(value int){
    s.stack = append(s.stack,value)
}

func (s *Stack)pop() int{

    if len(s.stack)>0{
        val := s.stack[len(s.stack)-1]
        s.stack=s.stack[:len(s.stack)-1]
        return val
    }

    return -1
}
