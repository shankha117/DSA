// https://leetcode.com/problems/diameter-of-binary-tree/description/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {

    ans := 0

    var findDiameter func(root *TreeNode) int

    findDiameter = func(root *TreeNode) int {

        if root == nil {
            return 0
        }

        dLeft := findDiameter(root.Left)
        dRight := findDiameter(root.Right)

        ans = max(ans, dLeft+dRight)

        return 1 + max(dLeft , dRight)

    }
    findDiameter(root)

    return ans


}
