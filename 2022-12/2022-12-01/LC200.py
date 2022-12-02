class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        land = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    land.add((i,j))

        def dfs(r,c):
            if (r,c) in land:
                land.discard((r,c))
                if 0 < r: dfs(r-1,c)
                if r+1 < m: dfs(r+1,c)
                if 0 < c: dfs(r,c-1)
                if c+1 < n: dfs(r,c+1)


        island = 0
        while land:
            y,x = land.pop()
            island += 1

            for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(y+dy,x+dx)

        return island