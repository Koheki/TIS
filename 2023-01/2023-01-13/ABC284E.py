from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
Graph = defaultdict(list)

for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    Graph[u].append(v)
    Graph[v].append(u)

lim = 10**6
visited = [False]*N
res = 0

def dfs(c):
    global res
    if res >= lim:
        return
    visited[c] = True
    res += 1
    for d in Graph[c]:
        if not visited[d]:
            dfs(d)
    visited[c] = False

dfs(0)
print(min(res,lim))