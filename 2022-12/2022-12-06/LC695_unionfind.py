class UnionFind:
    def __init__(self,grid,m,n):
        self.parent = [-1]*(m*n)
        self.size = [0]*(m*n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    p = i*n+j
                    self.parent[p] = p
                    self.size[p] = 1

    def root(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def unite(self,x,y):
        rootX, rootY = self.root(x), self.root(y)

        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

    def maxsize(self):
        return max(self.size)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        tree = UnionFind(grid,m,n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x = i*n+j

                    if 0 < i and grid[i-1][j] == 1: tree.unite(x,(i-1)*n+j)
                    if i+1 < m and grid[i+1][j] == 1: tree.unite(x,(i+1)*n+j) 
                    if 0 < j and grid[i][j-1] == 1: tree.unite(x,i*n+j-1)
                    if j+1 < n and grid[i][j+1] == 1: tree.unite(x,i*n+j+1)

        return tree.maxsize()