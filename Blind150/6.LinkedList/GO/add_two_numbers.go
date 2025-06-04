// https://leetcode.com/problems/add-two-numbers/description/
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	add := &ListNode{}

	ans := add

	carry, value := 0, 0

	for l1 != nil && l2 != nil {

		a, b := l1.Val, l2.Val

		carry, value = divmod(a+b+carry, 10)

		add.Next = &ListNode{Val: value}

		l1, l2, add = l1.Next, l2.Next, add.Next

	}

	for l1 != nil {

		carry, value = divmod(l1.Val+carry, 10)

		add.Next = &ListNode{Val: value}

		l1, add = l1.Next, add.Next

	}

	for l2 != nil {

		carry, value = divmod(l2.Val+carry, 10)

		add.Next = &ListNode{Val: value}

		l2, add = l2.Next, add.Next

	}

	if carry != 0 {

		add.Next = &ListNode{Val: carry}
	}

	return ans.Next

}

func divmod(a, b int) (int, int) {
	quotient := a / b
	remainder := a % b
	return quotient, remainder
}
