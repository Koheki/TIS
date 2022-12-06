class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        stack = []
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    stack.append((i,j))
                    size = 1

                    while stack:
                        y,x = stack.pop()

                        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                            if 0 <= y+dy < m and 0 <= x+dx < n and grid[y+dy][x+dx] == 1:
                                stack.append((y+dy,x+dx))
                                grid[y+dy][x+dx] = 0
                                size += 1
                    res = max(res,size)

        return res