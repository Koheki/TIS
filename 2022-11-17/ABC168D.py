from collections import deque

N,M = map(int,input().split())
G = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False for _ in range(N+1)]
visited[1] = True
res = [-1 for _ in range(N+1)]

que = deque([1])

while que:
    v = que.popleft()
    for g in G[v]:
        if not visited[g]:
            res[g] = v
            visited[g] = True
            que.append(g)

flag = True
for i in range(2,N+1):
    if res[i] == -1:
        flag = False
        break

if not flag:
    print("No")
else:
    print("Yes")
    for i in range(2,N+1):
        print(res[i])