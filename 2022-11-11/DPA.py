N = int(input())
H = [int(n) for n in input().split()]
inf = float("INF")
dp = [inf for _ in range(N)]
dp[0] = 0

for i in range(N-1):
    dp[i+1] = min(dp[i+1],dp[i]+abs(H[i+1] - H[i]))

    if i+2 < N:
        dp[i+2] = min(dp[i+2],dp[i]+abs(H[i+2] - H[i]))

print(dp[N-1])
