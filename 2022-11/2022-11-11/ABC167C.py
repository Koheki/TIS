N,M,X = map(int,input().split())

A = [[int(n) for n in input().split()] for _ in range(N)]
res = float("INf")

for i in range(1,1<<N):
    skill = [0 for _ in range(M)]
    c = 0
    for j in range(N):
        if (i>>j)&1:
            c += A[j][0]
            for k in range(M):
                skill[k] += A[j][k+1]

    flag = True
    for s in skill:
        if s < X:
            flag = False
            break
    if flag:
        res = min(res,c)

if res == float("INf"):
    print(-1)
else:
    print(res)
    
