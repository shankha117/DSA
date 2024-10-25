// https://leetcode.com/problems/top-k-frequent-elements/description/


import (
	"sort"
    "fmt"
)
func topKFrequent(nums []int, k int) []int {

        fMap := make(map[int]int)


        for _, ele := range nums {

            fMap[ele] ++

        }

        // Create a slice of keys, since maps don't have an inherent order
        keys := make([]int, 0, len(fMap))

        // Append all keys to the slice
        for key := range fMap {
            keys = append(keys, key)
        }

        // Sort the keys slice by values in the map
        sort.Slice(keys, func(i, j int) bool {
            return fMap[keys[i]] > fMap[keys[j]]
        })


        // fmt.Println(keys, fMap)

        ans := make([]int, 0, k)

        for i := range k {

            ans = append(ans, keys[i])

        }

        return ans




}
