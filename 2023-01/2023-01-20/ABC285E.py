N = int(input())
A = [int(n) for n in input().split()]

B = [0]*(N+1)
for i in range(1,N+1):
    B[i] = B[i-1] + A[((i+1)//2)-1]

minf = -float("INF")
dp = [[minf]*(N+1) for _ in range(N+1)]
dp[1][0] = 0

for i in range(1,N):
    for j in range(N+1):
        if dp[i][j] < 0:
            continue
        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j])
        dp[i+1][0] = max(dp[i+1][0],dp[i][j]+B[j])

res = 0
for i in range(N):
    res = max(res,dp[N][i]+B[i])

print(res)
