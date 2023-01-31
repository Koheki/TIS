N,X = map(int,input().split())
AB = [[int(n) for n in input().split()] for _ in range(N)]

dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(X+1):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True

        a,b = AB[i]
        c = j+a
        b -= 1
        while c <= X and b >= 0:
            dp[i+1][c] = True
            c += a
            b -= 1

if dp[N][X]:
    print("Yes")
else:
    print("No")

