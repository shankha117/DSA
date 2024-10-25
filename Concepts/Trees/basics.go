package main

import (
    "fmt"
)

type Node struct {
    value int
    left  *Node
    right *Node
}

// In-order Traversal
func inOrder(root *Node) {
    if root != nil {
        inOrder(root.left)
        fmt.Print(root.value, " ")
        inOrder(root.right)
    }
}

// Pre-order Traversal
func preOrder(root *Node) {
    if root != nil {
        fmt.Print(root.value, " ")
        preOrder(root.left)
        preOrder(root.right)
    }
}

// Post-order Traversal
func postOrder(root *Node) {
    if root != nil {
        postOrder(root.left)
        postOrder(root.right)
        fmt.Print(root.value, " ")
    }
}

// Level-order Traversal (BFS)
func levelOrder(root *Node) {
    if root == nil {
        return
    }

    // Use a slice as a queue and store a pointer to a Node , which is *Node
    // so root is basically a type of *Node
    queue := []*Node{root}

    fmt.Printf("The type of root is %T \n",root)

    for len(queue) > 0 {
        // Get the first element in the queue
        node := queue[0]
        queue = queue[1:] // Dequeue

        fmt.Print(node.value, " ")

        // Enqueue the left and right children if they exist
        if node.left != nil {
            queue = append(queue, node.left)
        }
        if node.right != nil {
            queue = append(queue, node.right)
        }
    }
}

func main() {
    root := &Node{value: 1}

    // level 1
    root.left = &Node{value:2}
    root.right = &Node{value:3}

    // level 2
    root.left.left = &Node{value:4}
    root.left.right = &Node{value:5}
    root.right.right = &Node{value:6}

    // level 3
    root.left.left.right = &Node{value:7}
    root.right.right.left = &Node{value:8}

    fmt.Println("In-order:")
    inOrder(root)  // Output: 4 2 5 1 3

    fmt.Println("\nPre-order:")
    preOrder(root)  // Output: 1 2 4 5 3

    fmt.Println("\nPost-order:")
    postOrder(root)  // Output: 4 5 2 3 1

    fmt.Println("\nLevel-order:")
    levelOrder(root)  // Output: 1 2 3 4 5
}
