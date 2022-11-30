class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        m = float('inf')
        profit =0

        for i in range(N):
            if prices[i] < m:
                m = prices[i]
            elif prices[i] - m > profit:
                profit = prices[i] - m

        return profit