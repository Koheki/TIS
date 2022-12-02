class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        dp = [0]*(n+1)
        dp[1] = dp[2] = 1

        for i in range(n):
            dp[i+1] += dp[i]
            if i+2 <= n:
                dp[i+2] += dp[i]
        return dp[n]