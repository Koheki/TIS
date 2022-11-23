H,N = map(int,input().split())
M = []

for _ in range(N):
    a,b = map(int,input().split())
    M.append([a,b])

inf = float("inf")
dp = [[inf for _ in range(H+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(H+1):
        a,b = M[i]
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        h = min(H,j+a)
        dp[i+1][h] = min(dp[i+1][h],dp[i+1][j]+b)

print(dp[N][H])
