class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        startcolor = image[sr][sc]
        image[sr][sc] = color
        m,n = len(image), len(image[0])
        visited = set()
        visited.add((sr,sc))
        stack = [[sr,sc]]

        while stack:
            r,c = stack.pop()

            for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
                x,y = c+dx,r+dy
                if 0 <= y < m and 0 <= x < n and image[y][x]== startcolor and (y,x) not in visited:
                    image[y][x] = color
                    stack.append([y,x])
                    visited.add((y,x))

        return image