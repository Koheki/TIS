N,W = map(int,input().split())
WV = [[int(n) for n in input().split()] for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        w,v = WV[i]
        if j < w:
            dp[i+1][j] = dp[i][j]
        if j+w <= W:
            dp[i+1][j+w] = max(dp[i][j]+v,dp[i][j+w])

print(max(dp[N]))