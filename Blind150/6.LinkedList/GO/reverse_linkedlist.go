
// https://leetcode.com/problems/reverse-linked-list/description/

 // Definition for singly-linked list.
 //
 type ListNode struct {
     Val int
     Next *ListNode
}


func reverseList(head *ListNode) *ListNode {

    prev, cur := (*ListNode)(nil) , head

    for cur != nil {

        tmp := cur.Next

        cur.Next = prev

        prev = cur

        cur = tmp


    }

    return prev

}
