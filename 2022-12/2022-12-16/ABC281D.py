N,K,D = map(int,input().split())
A = list(map(int,input().split()))

dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1,N+1):
    a = A[i-1]
    for k in range(K+1):
        for d in range(D):
            if dp[i-1][k-1][d] == -1:
                continue
            dp[i][k-1][d] = max(dp[i][k-1][d],dp[i-1][k-1][d])

            if k <= K:
                dp[i][k][(d+a)%D] = max(dp[i-1][k-1][d]+a,dp[i][k][(d+a)%D])

print(dp)
print(dp[N][K][0])

