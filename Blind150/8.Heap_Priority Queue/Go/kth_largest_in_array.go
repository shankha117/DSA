// https://leetcode.com/problems/kth-largest-element-in-an-array/description/
type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // 1st element is larger for max heap
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() any {

	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x

}

func findKthLargest(nums []int, k int) int {

	maxHeap := &MaxHeap{}

	*maxHeap = append(*maxHeap, nums...)

	heap.Init(maxHeap)

	for k > 1 {
		heap.Pop(maxHeap)
		k--
	}

	return heap.Pop(maxHeap).(int)

}
