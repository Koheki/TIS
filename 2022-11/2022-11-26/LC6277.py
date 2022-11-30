class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        onesRow = [ g.count(1) for g in grid]
        zerosRow = [g.count(0) for g in grid]
        onesCol =  [0 for _ in range(m)]
        zerosCol =  [0 for _ in range(m)]

        for i in range(m):
            one, zero = 0,0
            for j in range(n):
                if grid[j][i] == 1: one += 1
                else: zero += 1
            onesCol[i] = one
            zerosCol[i] = zero

        for i in range(n):
            for j in range(m):
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        return grid