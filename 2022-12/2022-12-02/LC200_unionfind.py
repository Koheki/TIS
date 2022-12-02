class UnionFind:
    def __init__(self,grid,m,n):
        self.parent = [-1]*(m*n)
        self.rank = [0]*(m*n)
        self.count = 0

        for i in range(m):
            for j in range(n):
                p = i*n+j
                if grid[i][j] == "1":
                    self.parent[p] = p
                    self.count += 1

    def root(self,p):
        if p != self.parent[p]:
            self.parent[p] = self.root(self.parent[p])
        return self.parent[p]
    
    def unite(self,p,q):
        rootP,rootQ = self.root(p),self.root(q)

        if rootP != rootQ:
            if self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            elif self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            else:
                self.parent[rootP] = rootQ
                self.rank[rootQ] += 1
            self.count -= 1

    def show(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        tree = UnionFind(grid,m,n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    if 0 <= i-1 and grid[i-1][j] == "1":
                        tree.unite(i*n+j,(i-1)*n+j)
                    if i+1 < m and grid[i+1][j] == "1":
                        tree.unite(i*n+j,(i+1)*n+j)
                    if 0 <= j-1 and grid[i][j-1] == "1":
                        tree.unite(i*n+j,i*n+j-1)
                    if j+1 < n and grid[i][j+1] == "1":
                        tree.unite(i*n+j,i*n+j+1)

        return tree.show()