class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        def dfs(r,c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                if 0 < r: dfs(r-1,c)
                if r+1 < m: dfs(r+1,c)
                if 0 < c: dfs(r,c-1)
                if c+1 < n: dfs(r,c+1)

        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i,j)

        return island