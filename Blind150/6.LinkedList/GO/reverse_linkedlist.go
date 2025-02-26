
// https://leetcode.com/problems/reverse-linked-list/description/

 // Definition for singly-linked list.
 //
 type ListNode struct {
     Val int
     Next *ListNode
}


func reverseList(head *ListNode) *ListNode {

	// why cant I simply use prev = nil becasue
	// In Go, when using `:=` with nil in a multiple assignment,
	// the compiler needs enough context to infer the type of `nil`. Since `nil` is untyped,
	// you must explicitly define the type for at least one variable to avoid ambiguity.


    prev, cur := (*ListNode)(nil) , head

    tmp := (*ListNode)(nil)

    for cur != nil {

        tmp = cur.Next

        cur.Next = prev

        prev = cur

        cur = tmp


    }

    return prev

}

```
The error `use of untyped nil in assignment` occurs because the Go compiler cannot infer the type of `nil` in this context. This typically happens when you're declaring multiple variables and `nil` is used without an explicit type.

### Problem:
In your code:


prev, cur := nil, head

The compiler can't deduce the type of `prev` because `nil` is untyped, and there's no other explicit information to infer its type.

### Solution:
You need to explicitly specify the type of `prev` as `*ListNode` to make it clear that `nil` is meant to represent a pointer to a `ListNode`. You can fix this as follows:

#### Option 1: Declare prev explicitly

var prev *ListNode
cur := head


#### Option 2: Cast nil to *ListNode

prev, cur := (*ListNode)(nil), head


### Updated Code:
Here's your corrected function:

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode // Explicitly declare prev as *ListNode
    cur := head

    for cur != nil {
        tmp := cur.Next
        cur.Next = prev
        prev = cur
        cur = tmp
    }

    return prev
}


### Why This Happens:

### Best Practice:
Always explicitly declare variables that are initialized to `nil` if their type isn't clear from the context. This ensures clarity and prevents such errors.


```
