class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            min_price = min(min_price,i)
            profit = i - min_price
            max_profit = max(max_profit,profit)
        return max_profit 
        