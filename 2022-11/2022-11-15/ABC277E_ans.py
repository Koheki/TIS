import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
G = [[[] for _ in range(N)] for _ in range(2)]
for _ in range(M):
    u, v, a = map(int, input().split())
    u -= 1; v -= 1
    G[a][u].append(v)
    G[a][v].append(u)

S = set(map(lambda x: int(x) - 1, input().split()))

que = deque([(1, 0, 0)])
visited = [[False] * N for _ in range(2)]
visited[1][0] = True
while que:
    state, node, dist = que.popleft()
    if node == N - 1:
        break
    for nxt in G[state][node]:
        if visited[state][nxt]: continue
        visited[state][nxt] = True
        que.append((state, nxt, dist + 1))

    if node not in S: continue
    state ^= 1
    for nxt in G[state][node]:
        if visited[state][nxt]: continue
        visited[state][nxt] = True
        que.append((state, nxt, dist + 1))

if node == N - 1:
    print(dist)
else:
    print(-1)

