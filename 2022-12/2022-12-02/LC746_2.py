class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        N = len(cost)
        memo = {}

        def cal(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            c1 = cost[i-1] + cal(i-1)
            c2 = cost[i-2] + cal(i-2)
            memo[i] = min(c1,c2)
            return memo[i]

        return cal(N)        
