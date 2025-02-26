// https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode) {

	s, f := head, head

	for f != nil && f.Next != nil {
		s = s.Next
		f = f.Next.Next

	}

	// find the head of the 2nd List
	snd := s.Next

	s.Next = nil

	// reverse the 2nd List
	prev, tmp := (*ListNode)(nil), (*ListNode)(nil)

	for snd != nil {

		tmp = snd.Next

		snd.Next = prev

		prev = snd

		snd = tmp

	}

	ft, sd := head, prev

	tmp1, tmp2 := (*ListNode)(nil), (*ListNode)(nil)

	for sd != nil {

		tmp1, tmp2 = ft.Next, sd.Next

		ft.Next = sd
		sd.Next = tmp1

		ft, sd = tmp1, tmp2

	}

}
