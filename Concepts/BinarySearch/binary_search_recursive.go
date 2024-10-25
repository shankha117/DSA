package main

import (
	"fmt"
)

func binarySearch(arr []int, low, high, target int) int {
	if high >= low {
		mid := low + (high-low)/2

		// Check if target is present at mid
		if arr[mid] == target {
			return mid
		}

		// If target is smaller, search in the left subarray
		if arr[mid] > target {
			return binarySearch(arr, low, mid-1, target)
		}

		// Otherwise, search in the right subarray
		return binarySearch(arr, mid+1, high, target)
	}

	// If target is not present
	return -1
}

func main() {
	arr := []int{2, 3, 4, 10, 40}
	target := 10
	result := binarySearch(arr, 0, len(arr)-1, target)
	if result != -1 {
		fmt.Printf("Element found at index %d\n", result)
	} else {
		fmt.Println("Element not found")
	}
}
