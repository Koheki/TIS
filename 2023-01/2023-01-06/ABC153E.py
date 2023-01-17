H,N = map(int,input().split())
AB = [[int(n) for n in input().split()] for _ in range(N)]

inf = float("INF")
dp = [[inf]*(H+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    a,b = AB[i]
    for j in range(H+1):
        # i 番目の魔法を選ばない場合
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])

        # i番目の魔法を1回以上選ぶ場合
        dp[i+1][min(H,j+a)] = min(dp[i+1][min(H,j+a)],dp[i+1][j]+b)

# print(dp)
print(dp[N][H])

