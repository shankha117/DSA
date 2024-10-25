// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

package main

func maxProfit(prices []int) int {

	if len(prices)<= 1{
		return 0
	}

	buy,sell := 0, 1

	prof := 0

	while sell < len(prices){

		if prices[buy] < prices[sell]{

			prof = max(prof, prices[sell] - prices[buy])

		}else{

			buy = sell
		}

		sell++

	}

	return prof

}
