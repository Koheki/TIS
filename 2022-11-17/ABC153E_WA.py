

H,N = map(int,input().split())
M = []

for _ in range(N):
    a,b = map(int,input().split())
    M.append([a,b])

inf = float("INF")
dp = [[inf for _ in range(H+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    a,b = M[i]
    for j in range(H+1):
        p = j+a
        if p > H:
            p = H
        dp[i+1][p] = min(dp[i][p],dp[i][j]+b)
        dp[i+1][p] = min(dp[i+1][p],dp[i+1][j]+b)

print(dp)
print(dp[N][H])

