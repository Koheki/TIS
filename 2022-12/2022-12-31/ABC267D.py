N,M = map(int,input().split())
A = [int(n) for n in input().split()]

inf = float("INF")
dp = [[-inf]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == -inf:
            continue
        # A[i] を選ばない
        dp[i+1][j] = max(dp[i][j],dp[i+1][j])
        # A[i] を選ぶ
        if j+1 <= M:
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+A[i]*(j+1))

print(dp[N][M])

