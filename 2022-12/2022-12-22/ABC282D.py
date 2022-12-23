from collections import defaultdict, deque

N,M = map(int,input().split())
Graph = defaultdict(list)

for _ in range(M):
    u,v = [int(n) -1 for n in input().split()]
    Graph[u].append(v)
    Graph[v].append(u)

color = [-1]*N
res = N*(N-1)//2 - M

for i in range(N):

    if color[i] != -1:
        continue
    que = deque([i])
    color[i] = 0
    white,black = 1,0
    while que:
        v = que.popleft()
        for g in Graph[v]:
            if color[g] != -1:
                if color[g] == color[v]:
                    print(0)
                    exit()
            else:
                color[g] = 1 - color[v]
                if color[g] == 0:
                    white+=1
                else:
                    black+=1
                que.append(g)

    res -= black*(black-1)//2
    res -= white*(white-1)//2

print(res)
