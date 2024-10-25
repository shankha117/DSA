// https://leetcode.com/problems/koko-eating-bananas/description/

// Helper function to determine if it's possible to eat all bananas in `h` hours at speed `k`
func canEat(piles []int, k, h int) bool {
	totalTime := 0
	for _, p := range piles {
		totalTime += int(math.Ceil(float64(p) / float64(k)))
	}
	return totalTime <= h
}

// Function to find the minimum eating speed that allows finishing all bananas within `h` hours
func minEatingSpeed(piles []int, h int) int {
	l, r := 1, maxInArray(piles)
	res := r

	for l <= r {
		mid := l + (r-l)/2
		if canEat(piles, mid, h) {
			res = min(res, mid)
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return res
}


// Helper function to find the maximum value in a slice
func maxInArray(arr []int) int {
	m := arr[0]
	for _, v := range arr {
		if v > m {
			m = v
		}
	}
	return m
}
