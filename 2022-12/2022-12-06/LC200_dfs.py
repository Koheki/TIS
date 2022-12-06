class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m,n = len(grid),len(grid[0])
        stack = []
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    stack.append((i,j))
                    grid[i][j] = '0'

                    while stack:
                        y,x = stack.pop()
                        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                            if 0 <= y+dy < m and 0 <= x+dx < n and grid[y+dy][x+dx] == '1':
                                stack.append((y+dy,x+dx))
                                grid[y+dy][x+dx] = '0'

                    res += 1

        return res