package main

import (
	"container/heap"
	"fmt"
)

// Task represents a task with priority
type Task struct {
    name     string
    priority int
}

// A TaskHeap implements heap.Interface and holds Tasks
type TaskHeap []Task

func (th TaskHeap) Len() int { return len(th) }
func (th TaskHeap) Less(i, j int) bool { return th[i].priority < th[j].priority } // Min-Heap based on priority
func (th TaskHeap) Swap(i, j int) { th[i], th[j] = th[j], th[i] }

func (th *TaskHeap) Push(x interface{}) {
    *th = append(*th, x.(Task))  // Cast to Task type
}

func (th *TaskHeap) Pop() interface{} {
    old := *th
    n := len(old)
    task := old[n-1]
    *th = old[0 : n-1]
    return task  // Return as Task type
}

func main() {
    tasks := &TaskHeap{
        {name: "Task1", priority: 3},
        {name: "Task2", priority: 1},
        {name: "Task3", priority: 2},
    }

    heap.Init(tasks)

    heap.Push(tasks, Task{name: "Task4", priority: 0})

    // Pop tasks in order of priority
    for tasks.Len() > 0 {
        task := heap.Pop(tasks).(Task)
        fmt.Printf("Task: %s, Priority: %d\n", task.name, task.priority)
    }
}
