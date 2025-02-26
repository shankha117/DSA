// https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
// implement the heap
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] } // Min-Heap; smaller one is at front
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	// The reason you need to type-assert x as int is that the heap.Interface in Go's container/heap package
	// is designed to work with interface{}. This means that methods like Push and Pop in your
	// custom heap implementation must work with values of type interface{}, which is the most general type in Go.
	// However, your heap is specifically intended to work with integers (int).
	// The append function in Go requires elements to be of a concrete type (e.g., int), not interface{}.
	// Therefore, you must assert the type of x to int before appending it to your slice of integers.

	*h = append(*h, x.(int)) // the reason we are using *h is because h is a pointer so ,
	// we need to dereference it
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1] // Get the last element which is the min ; kth largest element
	*h = old[0 : n-1]
	return x
}

// heap implementation is Done
type KthLargest struct {
	k    int
	nums *MinHeap
}

func Constructor(k int, nums []int) KthLargest {

	// Create the MinHeap and initialize it with the nums slice
	h := &KthLargest{
		k:    k,
		nums: &MinHeap{}, // Initialize nums as a MinHeap
	}

	*h.nums = append(*h.nums, nums...)

	// Initialize the heap
	heap.Init(h.nums)

	for h.nums.Len() > k {
		heap.Pop(h.nums) // h.nums is alreay a pointer
	}

	return *h // return the value of KthLargest

}

func (this *KthLargest) Add(val int) int {

	heap.Push(this.nums, val)

	if this.nums.Len() > this.k {

		heap.Pop(this.nums)
	}

	return (*this.nums)[0]
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */

// **** IMP ****
// 	Here's why you use h.Len() and heap.Pop(h) in different contexts:

// 1. h.Len() is a method of your custom Store type
// h.Len() directly accesses the Len method of your Store type, which is defined as:

// func (h Store) Len() int { return len(h) }

// Since Len() is part of your custom implementation, you can call it directly on h.

// 2. heap.Pop(h) is from the container/heap package
// heap.Pop(h) uses the heap.Interface, which relies on your custom Store to implement methods like Push, Pop, Less, etc.
// It ensures the heap property is maintained after an element is removed.

// The container/heap package manages the reordering of elements
// 	(e.g., calling Swap and Less as needed) and calls your custom Pop() only when appropriate.

// Simply calling h.Pop() bypasses the heap.Interface logic, which would break the heap's structure.

// Why you can't just use h.Pop(): ??

// h.Pop() removes the last element from your slice but doesn't maintain the heap property.
// heap.Pop(h) ensures that the smallest (or largest, depending on Less) element is removed and that the heap remains valid.
