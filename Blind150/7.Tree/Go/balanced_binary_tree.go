// https://leetcode.com/problems/balanced-binary-tree/description/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {

    isUnbalanced := false
	var checkBalance func(node *TreeNode) int
	checkBalance = func(node *TreeNode) int {
		if node == nil || isUnbalanced {
			return 0 // Return 0 for null nodes or stop further calculations if already unbalanced
		}

		leftHeight := checkBalance(node.Left)
		rightHeight := checkBalance(node.Right)

		if math.Abs(float64(leftHeight-rightHeight)) > 1 {
			isUnbalanced = true
		}

		return 1 + int(math.Max(float64(leftHeight), float64(rightHeight)))
	}

	checkBalance(root)

	return !isUnbalanced
}
