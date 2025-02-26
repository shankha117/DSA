// https://leetcode.com/problems/copy-list-with-random-pointer/description/
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {

	if head == nil {
		return nil
	}

	OldToCopy := make(map[*Node]*Node)

	cur := head

	for cur != nil {

		new := Node{Val: cur.Val}
		OldToCopy[cur] = &new
		cur = cur.Next

	}

	cur = head

	for cur != nil {

		copied := OldToCopy[cur]
		copied.Next = OldToCopy[cur.Next]
		copied.Random = OldToCopy[cur.Random]
		cur = cur.Next

	}

	return OldToCopy[head]

}
