N = int(input())
A = [int(n) for n in input().split()]
ans = 0
mod = 998244353

for i in range(1,N+1):
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    # 先頭 j 個から k 個選び、選んだ項の総和を i で割った余りが l となるものの個数を mod で割ったあまり
    for j in range(N):
        for k in range(i+1):
            for l in range(i):
                dp[j+1][k][l] += dp[j][k][l]
                dp[j+1][k][l] %= mod
                if k != i:
                    dp[j+1][k+1][(l+A[j])%i] += dp[j][k][l]
                    dp[j+1][k+1][(l+A[j])%i] %= mod
    ans += dp[N][i][0]
    ans %= mod
print(ans)

