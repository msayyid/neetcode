from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        
        return max_profit
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                profit = max(profit, prices[i] - prices[l])
        return profit
