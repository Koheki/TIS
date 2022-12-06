class UnionFind:
    def __init__(self,grid,m,n):
        self.parent = [0]*(m*n)
        self.rank = [1]*(m*n)
        self.count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    p = i*n + j
                    self.parent[p] = p
                    self.count += 1

    def root(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.root(x)
        rootY = self.root(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1


    def countisland(self):
        # print(self.parent)
        return self.count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        tree = UnionFind(grid,m,n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                        if 0 <= i+di < m and 0 <= j+dj < n  and grid[i+di][j+dj] == '1':
                            x = i*n+j
                            y = (i+di)*n+(j+dj)
                            tree.union(x,y)

        return tree.countisland()        