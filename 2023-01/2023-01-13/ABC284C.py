from collections import defaultdict, deque

N,M = map(int,input().split())
Graph = defaultdict(list)

for _ in range(M):
    u,v = map(int,input().split())
    Graph[u].append(v)
    Graph[v].append(u)

visited = set()
res = 0

for n in range(1,N+1):
    if n in visited:
        continue
    visited.add(n)
    res += 1
    que = deque([n])
    while que:
        v = que.popleft()
        for g in Graph[v]:
            if g not in visited:
                visited.add(g)
                que.append(g)

print(res)
