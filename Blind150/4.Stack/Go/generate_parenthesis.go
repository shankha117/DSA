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
