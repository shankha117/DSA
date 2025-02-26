// https://leetcode.com/problems/subtree-of-another-tree/description/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSameTree(p *TreeNode, q *TreeNode) bool {

	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil || p.Val != q.Val {
		return false
	}

	if isSameTree(p.Left, q.Left) == false || isSameTree(p.Right, q.Right) == false {

		return false
	}

	return true

}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {

	if root == nil {
		return false
	}

	queue := []*TreeNode{root}
	var possibleRoots []*TreeNode

	for len(queue) > 0 {

		c := queue[0] // take the 1st element

		queue = queue[1:]

		if c.Val == subRoot.Val {
			possibleRoots = append(possibleRoots, c)
		}

		if c.Left != nil {

			queue = append(queue, c.Left)
		}

		if c.Right != nil {

			queue = append(queue, c.Right)
		}

	}

	for i := len(possibleRoots) - 1; i >= 0; i-- {

		if isSameTree(possibleRoots[i], subRoot) {
			return true
		}
	}

	return false

}
