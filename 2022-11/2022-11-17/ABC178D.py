S = int(input())
mod = 10**9+7

if S < 3:
    print(0)
    exit()

dp = [1 for _ in range(S+1)]
dp[0],dp[1],dp[2] = 0,0,0

for i in range(3,S+1):
    for j in range(3,S+1):
        if i+j <= S:
            dp[i+j] += dp[i]
            dp[i+j] %= mod

print(dp[S])
