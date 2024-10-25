// https://leetcode.com/problems/generate-parentheses/description/
func generateParenthesis(n int) []string {
    var ans []string

	var backtrack func(op, cl int, st string)
	backtrack = func(op, cl int, st string) {
        if op == n && cl == n {

            ans = append(ans, st)
            return
        }

        if op < n {

            backtrack(op+1, cl , st+"(")
        }

        if cl < op {

            backtrack(op, cl+1 , st+")")
        }


    }

    backtrack(0,0, "")

    return ans


}

// ***IMP
// Why this approach?
// In Go, recursive function variables need to be declared first because Go requires that the
// function variable (in this case, backtrack) is known to exist when you reference it recursively within its body.

// If you skip the explicit declaration step and write it as:

// backtrack := func(op, cl int, st string) {
// It won't work for recursion. This shorthand would create a new local variable backtrack that shadows any other variable
// with the same name, meaning you can't reference backtrack within its own body for recursion purposes. Therefore, declaring
// backtrack first allows Go to recognize that it refers to the same recursive function throughout its scope.
