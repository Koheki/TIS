N,M = map(int,input().split())

G = {i:[] for i in range(N)}

for _ in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)

res = 0
for i in range(N):
    visted = [False for _ in range(N)]
    visted[i] = True
    stack = [i]
    res += 1

    while stack:
        v = stack.pop()
        for j in G[v]:
            if not visted[j]:
                stack.append(j)
                visted[j] = True
                res += 1

print(res)

