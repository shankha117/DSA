// https://leetcode.com/problems/task-scheduler/description/
type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
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

func leastInterval(tasks []byte, n int) int {

	// Step 1: Count task frequencies
	taskArrival := map[string]int{}
	for _, task := range tasks {
		taskArrival[string(task)]++
	}

	// Step 2: Initialize other variables
	nextTaskMap := map[int]int{}
	t := 0
	totalTaskCount := len(taskArrival)

	// Step 3: Initialize the MaxHeap
	maxHeap := &MaxHeap{}
	heap.Init(maxHeap)

	for _, count := range taskArrival {
		heap.Push(maxHeap, count)
	}

	for totalTaskCount > 0 {

		t += 1

		if taskValue, exists := nextTaskMap[t]; exists {
			heap.Push(maxHeap, taskValue)
		}

		if maxHeap.Len() > 0 {

			ct := heap.Pop(maxHeap).(int)

			if ct-1 == 0 {
				totalTaskCount -= 1
			} else {
				nextTaskMap[t+n+1] = ct - 1
			}
		}
	}

	return t

}
