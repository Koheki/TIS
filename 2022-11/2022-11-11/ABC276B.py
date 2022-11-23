N,M = map(int,input().split())

d = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

for i in range(1,N+1):
    d[i].sort()
    n = len(d[i])

    if n == 0:
        print(0)
    else:
        print(n,*d[i])

