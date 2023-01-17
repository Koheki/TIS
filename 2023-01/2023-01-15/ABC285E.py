N = int(input())
A = [int(n) for n in input().split()]

inf = float("INF")
dp = [[[inf]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = [0,0]

for i in range(N):
    dp[i+1][0] = 0
    for j in range(1,N+1):
        for k in range(2):
            



