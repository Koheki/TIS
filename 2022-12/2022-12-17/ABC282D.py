import collections

N,M = map(int,input().split())
G = collections.defaultdict(list)
path = collections.defaultdict(int)
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    path[u] += 1
    path[v] += 1

color = [-1]*N
res = N*(N-1)//2 - M
judge = True
white,black = 0,0

for u in range(N):
    if color[u] == -1:
        que = collections.deque([u])
        color[u] = 0
        white += 1
        while que and judge:
            v = que.pop()
            for g in G[v]:
                if color[g] != -1:
                    if color[v] == color[g]:
                        print(0)
                        exit()
                else:
                    color[g] = 1 - color[v]
                    que.append(g)
                    if color[g] == 0:
                        white += 1
                    else:
                        black += 1
    res -= white*(white-1)//2
    res -= black*(black-1)//2

print(res)
