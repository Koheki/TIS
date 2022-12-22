class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minval= prices[0]
        n = len(prices)
        for i in range(1,n):
            if prices[i] - minval > profit:
                profit = prices[i] - minval
            if prices[i] < minval:
                minval = prices[i]

        return profit