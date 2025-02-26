
// https://leetcode.com/problems/k-closest-points-to-origin/description/

type Point struct {
	X int
	Y int
}

func getDistanceFromOrigin(x, y int) int {
	return (x * x) + (y * y)
}

func kClosest(points [][]int, k int) [][]int {

	// Initialize MinHeap struct as an empty slice
	minHeap := &MinHeap{}

	for _, val := range points {

		*minHeap = append(*minHeap, HeapItem{
			Distance: getDistanceFromOrigin(val[0], val[1]),
			Point:    Point{X: val[0], Y: val[1]},
		})
	}

	// Convert the slice into a valid heap
	heap.Init(minHeap)

	// create an empty({}) slice of list of lists
	result := [][]int{}

	for k > 0 && minHeap.Len() > 0 {

		// we need to use the () after `.` ; else we get
		// Line 34: Char 35: heap.Pop(minHeap).HeapItem undefined (type any has no field or method HeapItem) (solution.go)
		// becasue When you try to access .HeapItem directly on heap.Pop(minHeap),
		// Go doesn't know the underlying type of the value returned by heap.Pop, so it raises an error.
		// so, we need to typeassert similar to `x.(int)`
		item := heap.Pop(minHeap).(HeapItem)
		result = append(result, []int{item.Point.X, item.Point.Y})
		k--

	}

	return result
}

// Define the MinHeap
type HeapItem struct {
	Distance int
	Point    Point
}

type MinHeap []HeapItem

// define the methods required for Go's `container/heap` package
func (h MinHeap) Len() int { return len(h) }

func (h MinHeap) Less(i, j int) bool { return h[i].Distance < h[j].Distance }

func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(HeapItem))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[0 : n-1]
	return item
}
