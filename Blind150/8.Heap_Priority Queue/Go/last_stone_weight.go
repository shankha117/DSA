// https://leetcode.com/problems/last-stone-weight/description/
type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] } // 1st element is larger for max heap
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *maxHeap) Pop() any {

	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x

}

func lastStoneWeight(stones []int) int {
	// Create and initialize the heap
	h := &maxHeap{}
	heap.Init(h)

	// Add all stones to the max-heap
	for _, stone := range stones {
		heap.Push(h, stone)
	}

	// Process the stones
	for h.Len() > 1 {
		// Pop the two largest stones
		stone1 := heap.Pop(h).(int)
		stone2 := heap.Pop(h).(int)

		// If they are not equal, push the difference back into the heap
		if stone1 != stone2 {
			heap.Push(h, stone1-stone2)
		}
	}

	// Return the last remaining stone or 0 if none
	if h.Len() == 1 {
		return heap.Pop(h).(int)
	}
	return 0
}
