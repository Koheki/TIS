N,X,Y = map(int,input().split())

dp = [[0,0] for _ in range(N)]
dp[0][0] = 1

for i in range(1,N):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]*Y
    dp[i][1] = dp[i-1][1] + dp[i][0]*X

print(dp[N-1][1])

