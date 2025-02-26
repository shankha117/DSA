// https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {

	var elems []int

	var inorder func(root *TreeNode)

	inorder = func(root *TreeNode) {

		if root == nil {
			return
		}

		inorder(root.Left)

		if len(elems) == k {
			return
		}

		elems = append(elems, root.Val)

		inorder(root.Right)
	}

	inorder(root)

	return elems[len(elems)-1]

}
