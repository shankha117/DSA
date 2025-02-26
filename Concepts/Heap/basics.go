package main

import (
	"container/heap"
	"fmt"
)

// Define a MinHeap type that implements heap.Interface
type MinHeap []int

// Len is part of sort.Interface. Returns the number of elements in the heap.
func (h MinHeap) Len() int {
	return len(h)
}

// Less is part of sort.Interface. Returns true if the element at index i is smaller than the element at index j.
func (h MinHeap) Less(i, j int) bool {
	return h[i] < h[j] // Min-heap property: smallest element at root
}

// Swap is part of sort.Interface. Swaps the elements at index i and j.
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push is part of heap.Interface. Adds an element to the heap.
// After adding, the heap may violate the heap property, so the heap must "bubble"
// the new element to its correct position.
// This is done by the heap.Push function from the container/heap package,
// which will reorder the heap.
// We append the new element x (which is type-asserted to an int) to the heap.
// The heap package handles the internal reordering (heapifying) to maintain the heap property.
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int)) // Type assertion to convert interface{} to int
}

// Pop is part of heap.Interface. Removes and returns the smallest element.
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]     // Get the last element
	*h = old[0 : n-1] // Reduce the slice size
	return x
}

func (h *MinHeap) NthLargest(n int) int {
	tempHeap := &MinHeap{}
	heap.Init(tempHeap)
	for _, num := range *h {
		heap.Push(tempHeap, num)
		if tempHeap.Len() > n {
			heap.Pop(tempHeap)
		}
	}
	return heap.Pop(tempHeap).(int)
}

func (h *MinHeap) NthSmallest(n int) int {
	maxHeap := &MaxHeap{}
	heap.Init(maxHeap)
	for _, num := range *h {
		heap.Push(maxHeap, num)
		if maxHeap.Len() > n {
			heap.Pop(maxHeap)
		}
	}
	return heap.Pop(maxHeap).(int)
}

func (h *MinHeap) Smallest() int {
	if h.Len() == 0 {
		panic("Heap is empty")
	}
	return (*h)[0]
}

func (h *MinHeap) Largest() int {
	if h.Len() == 0 {
		panic("Heap is empty")
	}
	max := (*h)[0]
	for _, val := range *h {
		if val > max {
			max = val
		}
	}
	return max
}

// MaxHeap structure
type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// Main function demonstrating the usage of heap functions
func main() {
	// Create a MinHeap and initialize it
	h := &MinHeap{5, 10, 3, 8}
	heap.Init(h) // Heapify the slice to maintain the heap property

	fmt.Println("Initial heap:", *h) // Output: [3 8 5 10]

	// Push elements into the heap
	heap.Push(h, 2)
	heap.Push(h, 7)
	fmt.Println("Heap after pushes:", *h) // Output: [2 3 5 10 8 7]

	// Pop the smallest element
	fmt.Println("Popped element:", heap.Pop(h)) // Output: 2
	fmt.Println("Heap after pop:", *h)          // Output: [3 7 5 10 8]

	// Remove an element at a specific index
	heap.Remove(h, 2)                      // Removes the element at index 2
	fmt.Println("Heap after removal:", *h) // Output: [3 7 8 10]

	// Push-Pop example
	fmt.Println("Push-Pop result:", heap.PushPop(h, 4)) // Output: 3
	fmt.Println("Heap after Push-Pop:", *h)             // Output: [4 7 8 10]

	// Replace example
	fmt.Println("Replace result:", heap.Replace(h, 6)) // Output: 4
	fmt.Println("Heap after Replace:", *h)             // Output: [6 7 8 10]
}

// Why Use &?
// - The heap package operates on a pointer to the heap because modifying the heap
// 	(e.g., adding or removing elements) requires updating the underlying
// 	data structure in place.
// - By passing a pointer, the methods can directly modify the original heap
// 	instead of working on a copy.

// In Go, when you create a variable like MinHeap{5, 10, 3, 8},
// it creates a value of type MinHeap. If you want to allow modifications to this heap
// from another part of the program, you must work with a pointer.

// Notice the receiver (h *MinHeap) for Push and Pop.
// - The *MinHeap receiver indicates that these methods modify the original heap.
// - If you don't pass a pointer to heap.Push or heap.Pop,
// these methods can't update the actual heap in memory, only a copy of it.

// What Happens Under the Hood?

// Memory Allocation: &MinHeap{5, 10, 3, 8} allocates a MinHeap in memory and
// 					returns a pointer to it.

// Pointer Passing: When you pass h to heap.Init(h) or similar functions, you are
// passing a pointer. Functions like Push and Pop then use this pointer to directly
// modify the original heap.

// Efficiency: Passing a pointer is more efficient than passing large data
// structures by value, especially when dealing with complex or large heaps.
