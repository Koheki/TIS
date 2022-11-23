N,X = map(int,input().split())

VP = [[int(n) for n in input().split()] for _ in range(N)]
X *= 100
res = -1
for i in range(N):
    v,p = VP[i]
    X -= v*p

    if X < 0:
        res = i+1
        break

print(res)
