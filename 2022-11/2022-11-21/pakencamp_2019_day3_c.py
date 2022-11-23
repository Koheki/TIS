N,M = map(int,input().split())

A = [[int(n) for n in input().split()] for _ in range(N)]

res = 0
for t1 in range(M):
    for t2 in range(t1+1,M):
        score = 0
        for i in range(N):
            score += max(A[i][t1],A[i][t2])
        res = max(res,score)

print(res)
