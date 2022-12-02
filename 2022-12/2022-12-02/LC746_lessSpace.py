class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        d1,d2 = 0,0
        for i in range(2,N+1):
            tmp = d1
            d1 = min(d1+cost[i-1],d2+cost[i-2])
            d2 = tmp

        return d1