import pprint

def ford_fullkerson(V, Graph, source, sink):
    maxflow = 0
    def dfs_ff(s,e,flow):
        if s == e:
            return flow
        visited[s] = True
        for i in range(V):
            if not visited[i] and Graph[s][i]> 0:
                f = dfs_ff(i,e,min(flow,Graph[s][i]))
                if f > 0:
                    Graph[s][i] -= f
                    Graph[i][s] += f
                    return f
        return 0

    while True:
        visited = [False]*V
        f = dfs_ff(source,sink,10**9)
        print(f)
        pprint.pprint(Graph)
        if f == 0:
            return maxflow
        maxflow += f
    return 0


capacity =[
[0, 10, 10, 0, 0, 0],
[0, 0, 0, 4, 8, 0],
[0, 0, 0, 7, 4, 0],
[0, 0, 0, 0, 0, 8],
[0, 0, 0, 0, 0, 12],
[0, 0, 0, 0, 0, 0]
]

pprint.pprint(capacity)

print(ford_fullkerson(6,capacity,0,5))