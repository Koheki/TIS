import sys
from collections import defaultdict,deque

input = sys.stdin.readline

N,M,K = map(int,input().split())
G = defaultdict(list)

for _ in range(M):
    v1,v2,a = map(int,input().split())
    if a:
        G[v1].append([v2,1])
        G[v2].append([v1,1])
    else:
        G[N+v1].append([N+v2,1])
        G[N+v2].append([N+v1,1])

S = [int(n) for n in input().split()]

for s in S:
    G[s].append([N+s,0])
    G[N+s].append([s,0])

que = deque([1])
inf = 10**9
dist = [inf for _ in range(2*N+1)]
dist[1] = 0

while que:
    v = que.popleft()
    for g,c in G[v]:
        if dist[g] > dist[v]+c:
            dist[g] = dist[v]+c
            if c == 0:
                que.appendleft(g)
            else:
                que.append(g)

res = min(dist[N],dist[2*N])
if res == inf: print(-1)
else: print(res)
