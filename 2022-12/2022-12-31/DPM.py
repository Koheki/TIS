N,K = map(int,input().split())
A = [int(n) for n in input().split()]
mod = 10**9+7

dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):
    a = A[i-1]
    sums = [0]*(K+2)
    for j in range(1,K+2):
        sums[j] = dp[i-1][j-1] + sums[j-1]

    for k in range(K+1):
        sums_i = k+1
        dp[i][k] = (sums[sums_i]-sums[max(sums_i-a-1,0)]) % mod

print(dp[N][K]%mod)