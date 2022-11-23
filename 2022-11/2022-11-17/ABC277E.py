from collections import deque

N,M,K = map(int,input().split())

G = {i:[] for i in range(1,2*N+1)}

for _ in range(M):
    v1,v2,a = map(int,input().split())

    if a:
        G[v1].append([v2,1])
        G[v2].append([v1,1])
    else:
        G[v1+N].append([N+v2,1])
        G[v2+N].append([N+v1,1])

S = [int(n) for n in input().split()]

for s in S:
    G[s].append([s+N,0])
    G[s+N].append([s,0])

inf = float('inf')
dist = [inf for _ in range(1,2*N+1)]
dist[1] = 0

que = deque([1])

while que:
    v = que.popleft()
    for g,c in G[v]:
        if dist[g] > dist[v]+c:
            dist[g] = dist[v]+c
            
            if c:
                que.append(g)
            else:
                que.appendleft(g)
print(-1)