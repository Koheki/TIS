import heapq

N,M = map(int,input().split())
Graph = {i:[] for i in range(N)}

for i in range(1,M+1):
    a,b,c = map(lambda x:int(x) -1,input().split())
    Graph[a].append([b,c,i])
    Graph[b].append([a,c,i])

inf = float("INF")
visited = set()
dist = [inf]*N
dist[0] = 0

idx = [0]*N

node = []
heapq.heappush(node,[0,0])

while node:
    _,cur = heapq.heappop(node)
    if cur not in visited:
        for v,w,p in Graph[cur]:
            if dist[v] > dist[cur] + w:
                dist[v] = dist[cur]+w
                heapq.heappush(node,[dist[v],v])
                idx[v] = p
        visited.add(cur)

print(*idx[1::])
