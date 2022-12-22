class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        valley,peak = prices[0],prices[0]
        res = 0
        i = 0
        while i+1 < n:
            while i+1 < n and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i+1 < n and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            res += peak - valley

        return res
