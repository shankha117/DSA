package main

import "fmt"

type node struct {
	data int
	next *node
}

type linkedList struct {
	head   *node
	tail   *node
	length int
}

func (l *linkedList) prepend(n *node) {
	// If the list is empty, both head and tail point to the new node

	if l.head == nil {
		l.head = n
		l.tail = n
	} else {

		n.next = l.head
		l.head = n
	}

	// second := l.head

	// l.head = n

	// l.head.next = second

	l.length++

}

func (l linkedList) pritnList() {

	toPrint := l.head

	for toPrint != nil {

		fmt.Printf("%v ", toPrint.data)
		toPrint = toPrint.next
	}
	fmt.Println()

}

func (l *linkedList) append(n *node) {

	if l.head == nil {
		// If the list is empty, both head and tail point to the new node
		l.head = n
		l.tail = n
	} else {

		l.tail.next = n
		l.tail = n
	}

	l.length++

}

func (l *linkedList) deleteWithValue(value int) {

	prevToDelete := l.head

	// handle deletion of head node
	if l.head.data == value {
		l.head = l.head.next
		l.length--
		return
	}

	// handle deletion single node linked list``
	if l.length == 0 {
		fmt.Println(" No linked list found")
		return

	}

	for prevToDelete.next.data != value {

		prevToDelete = prevToDelete.next

		if prevToDelete.next == nil {
			fmt.Printf("no node found with data %v \n", value)
			return
		}

	}

	prevToDelete.next = prevToDelete.next.next

}

func main() {

	list1 := linkedList{}

	node1 := node{data: 10}
	node2 := node{data: 11}
	node3 := node{data: 12}

	list1.prepend(&node1)
	list1.prepend(&node2)
	list1.prepend(&node3)

	node4 := node{data: 13}
	node5 := node{data: 14}
	node6 := node{data: 15}

	list1.append(&node4)
	list1.append(&node5)
	list1.append(&node6)

	list1.pritnList()

	list1.deleteWithValue(12)

	list1.pritnList()

	list1.deleteWithValue(120)

	list1.pritnList()

}
