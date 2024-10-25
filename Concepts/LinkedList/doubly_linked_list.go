package main

import "fmt"

type node struct {
	data int
	next *node
	prev *node // Adding prev to create a doubly linked list
}

type linkedList struct {
	head   *node
	tail   *node
	length int
}

// Prepend a node to the list
func (l *linkedList) prepend(n *node) {
	if l.head == nil {
		l.head = n
		l.tail = n
	} else {
		n.next = l.head
		l.head.prev = n
		l.head = n
	}
	l.length++
}

// Print the list
func (l linkedList) printList() {
	toPrint := l.head
	for toPrint != nil {
		fmt.Printf("%v ", toPrint.data)
		toPrint = toPrint.next
	}
	fmt.Println()
}

// Append a node to the list
func (l *linkedList) append(n *node) {
	if l.head == nil {
		l.head = n
		l.tail = n
	} else {
		l.tail.next = n
		n.prev = l.tail
		l.tail = n
	}
	l.length++
}

// Delete a node with a specific value
func (l *linkedList) deleteWithValue(value int) {
	if l.head == nil {
		fmt.Println("No linked list found")
		return
	}

	if l.head.data == value {
		if l.head.next != nil {
			l.head = l.head.next
			l.head.prev = nil
		} else {
			l.head = nil
			l.tail = nil
		}
		l.length--
		return
	}

	toDelete := l.head
	for toDelete != nil && toDelete.data != value {
		toDelete = toDelete.next
	}

	if toDelete == nil {
		fmt.Printf("No node found with data %v\n", value)
		return
	}

	if toDelete.next != nil {
		toDelete.next.prev = toDelete.prev
	} else {
		l.tail = toDelete.prev
	}

	toDelete.prev.next = toDelete.next

	// if toDelete.prev != nil {

	// }

	l.length--
}

func main() {
	list1 := linkedList{}

	fmt.Println("Test Case 1: Initial List (should be empty)")
	list1.printList()

	fmt.Println("\nTest Case 2: Deleting from an empty list")
	list1.deleteWithValue(10)
	list1.printList() // No output expected

	fmt.Println("\nTest Case 3: Adding and removing a single node")
	node1 := &node{data: 10}
	list1.prepend(node1)
	list1.printList() // Expected: 10
	list1.deleteWithValue(10)
	list1.printList() // Expected: empty list

	fmt.Println("\nTest Case 4: Adding nodes to the list")
	node2 := &node{data: 20}
	node3 := &node{data: 30}
	list1.prepend(node2)
	list1.append(node3)
	list1.printList() // Expected: 20 30

	fmt.Println("\nTest Case 5: Deleting the head node")
	list1.deleteWithValue(20)
	list1.printList() // Expected: 30

	fmt.Println("\nTest Case 6: Deleting the tail node")
	node4 := &node{data: 40}
	list1.append(node4)
	list1.printList() // Expected: 30 40
	list1.deleteWithValue(40)
	list1.printList() // Expected: 30

	fmt.Println("\nTest Case 7: Adding multiple nodes to the list")
	node5 := &node{data: 50}
	node6 := &node{data: 60}
	node7 := &node{data: 70}
	list1.append(node5)
	list1.prepend(node6)
	list1.append(node7)
	list1.printList() // Expected: 60 30 50 70

	fmt.Println("\nTest Case 8: Deleting a middle node")
	list1.deleteWithValue(50)
	list1.printList() // Expected: 60 30 70

	fmt.Println("\nTest Case 9: Deleting head node when multiple nodes are present")
	list1.deleteWithValue(60)
	list1.printList() // Expected: 30 70

	fmt.Println("\nTest Case 10: Sequential deletions")
	list1.deleteWithValue(30)
	list1.deleteWithValue(70)
	list1.printList() // Expected: empty list

	fmt.Println("\nTest Case 11: Adding nodes again after deletions")
	node8 := &node{data: 80}
	node9 := &node{data: 90}
	list1.prepend(node8)
	list1.append(node9)
	list1.printList() // Expected: 80 90

	fmt.Println("\nTest Case 12: Deleting a node not present in the list")
	list1.deleteWithValue(100) // Should print a message
	list1.printList()          // Expected: 80 90

	fmt.Println("\nTest Case 13: Deleting the last remaining node")
	list1.deleteWithValue(90)
	list1.deleteWithValue(80)
	list1.printList() // Expected: empty list

	fmt.Println("\nTest Case 14: Adding nodes in complex order")
	node10 := &node{data: 100}
	node11 := &node{data: 110}
	node12 := &node{data: 120}
	list1.append(node10)
	list1.prepend(node11)
	list1.append(node12)
	list1.printList() // Expected: 110 100 120

	fmt.Println("\nTest Case 15: Mixed appends and prepends")
	node13 := &node{data: 130}
	node14 := &node{data: 140}
	list1.prepend(node13)
	list1.append(node14)
	list1.printList() // Expected: 130 110 100 120 140

	fmt.Println("\nTest Case 16: Deleting multiple nodes")
	list1.deleteWithValue(100)
	list1.deleteWithValue(110)
	list1.deleteWithValue(130)
	list1.printList() // Expected: 120 140

	fmt.Println("\nTest Case 17: Adding nodes in between deletions")
	node15 := &node{data: 150}
	node16 := &node{data: 160}
	list1.prepend(node15)
	list1.append(node16)
	list1.printList() // Expected: 150 120 140 160

	fmt.Println("\nTest Case 18: Deleting all nodes")
	list1.deleteWithValue(150)
	list1.deleteWithValue(120)
	list1.deleteWithValue(140)
	list1.deleteWithValue(160)
	list1.printList() // Expected: empty list
}
