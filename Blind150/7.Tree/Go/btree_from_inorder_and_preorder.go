// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {

	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}

	root := &TreeNode{Val: preorder[0]}

	mid := 0

	for pos, val := range inorder {

		if val == root.Val {
			mid = pos
			break
		}
	}

	// Split inorder and preorder lists
	inorderLeft, inorderRight := inorder[:mid], inorder[mid+1:]
	preorderLeft, preorderRight := preorder[1:len(inorderLeft)+1], preorder[len(inorderLeft)+1:]

	root.Left = buildTree(preorderLeft, inorderLeft)
	root.Right = buildTree(preorderRight, inorderRight)

	return root

}
