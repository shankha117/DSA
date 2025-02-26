// https://leetcode.com/problems/merge-two-sorted-lists/description/


 // Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

    tmp := &ListNode{}
    head := tmp

    for list1 != nil && list2 != nil{
        if list1.Val >list2.Val{
            tmp.Next = list2
            list2 = list2.Next
        }else{
            tmp.Next = list1
            list1 = list1.Next
        }
        tmp = tmp.Next
    }


    if list1 != nil {
        tmp.Next = list1
    }else{
        tmp.Next = list2
    }

    return head.Next

}
