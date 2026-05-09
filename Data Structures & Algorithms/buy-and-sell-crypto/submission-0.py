class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        max_profit = 0
        current_profit = 0
        while end < len(prices):
            current_profit = prices[end] - prices[start]
            if current_profit <= 0:
                start = end
            elif current_profit > max_profit:
                max_profit = current_profit
            end +=1
        return max_profit
            
                