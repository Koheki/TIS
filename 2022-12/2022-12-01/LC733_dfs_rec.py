class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        startcolor = image[sr][sc]
        m,n = len(image), len(image[0])

        def dfs(r,c):
            if image[r][c] == startcolor:
                image[r][c] = color

                if 0 < r: dfs(r-1,c)
                if r+1 < m: dfs(r+1,c)
                if 0 < c: dfs(r,c-1)
                if c+1 < n: dfs(r,c+1)

        dfs(sr,sc)
        return image