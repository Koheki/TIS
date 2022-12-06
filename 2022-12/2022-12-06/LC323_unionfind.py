class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*(n)
        self.count = n

    def root(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX,rootY = self.root(x),self.root(y)

        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.count -= 1

    def show(self):
        return self.count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        tree = UnionFind(n)
        Graph = collections.defaultdict(list)
        for u,v in edges:
            Graph[u].append(v)
            Graph[v].append(u)

        for v in range(n):
            if v in Graph:
                for g in Graph[v]:
                    tree.union(v,g)

        return tree.show()
