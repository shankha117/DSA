// https://leetcode.com/problems/binary-tree-level-order-traversal/description/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {

	if root == nil {
		return [][]int{}
	}

	dq := []*TreeNode{root}
	result := [][]int{}

	for len(dq) > 0 {

		levelList := []int{}
		levelSize := len(dq)

		for i := 0; i < levelSize; i++ {

			curNode := dq[0] // take the first from left from the queue

			dq = dq[1:] // remove the first element from the queue

			levelList = append(levelList, curNode.Val)

			if curNode.Left != nil {

				dq = append(dq, curNode.Left)
			}

			if curNode.Right != nil {

				dq = append(dq, curNode.Right)
			}

		}

		result = append(result, levelList)

	}

	return result

}
