class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        startcolor = image[sr][sc]
        image[sr][sc] = color
        m,n = len(image), len(image[0])
        visited = set()
        visited.add((sr,sc))
        que = collections.deque([[sr,sc]])

        while que:
            r,c = que.popleft()

            for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
                x,y = c+dx,r+dy
                if 0 <= y < m and 0 <= x < n and image[y][x]== startcolor and not visited[y][x]:
                    image[y][x] = color
                    que.append([y,x])
                    visited.add((y,x))

        return image
