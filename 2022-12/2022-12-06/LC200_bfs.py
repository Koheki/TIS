class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        que = collections.deque()
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    que.append((i,j))
                    grid[i][j] = '0'

                    while que:
                        y,x = que.popleft()

                        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):

                            if 0 <= y+dy < m and 0 <= x+dx < n and grid[y+dy][x+dx] == '1':
                                que.append((y+dy,x+dx))
                                grid[y+dy][x+dx] = '0'
                    res += 1
        
        return res