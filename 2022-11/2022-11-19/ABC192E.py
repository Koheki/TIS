import heapq

def dijkstra(G,V,s,g):
    inf = float("inf")
    visited = [False] * (V+1)
    dist = [inf] * (V+1)
    dist[s] = 0

    que = []
    heapq.heappush(que,[0,s])

    while que:
        _,cur = heapq.heappop(que)

        if not visited[cur]:
            for v, t, k in G[cur]:
                w = dist[cur]%k
                if w != 0:
                    w = k - w
                if dist[v] > dist[cur] + w + t:
                    dist[v] = dist[cur] + w + t
                    heapq.heappush(que,[dist[v],v])

            visited[cur] = True

    if dist[g] == inf:
        return -1
    else:
        return dist[g]

N,M,X,Y = map(int,input().split())

Graph = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b,t,k = map(int,input().split())
    Graph[a].append([b,t,k])
    Graph[b].append([a,t,k])

print(dijkstra(Graph,N,X,Y))