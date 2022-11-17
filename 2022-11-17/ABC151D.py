from collections import deque

H,W = map(int,input().split())

S = [[s for s in input()] for _ in range(H)]

def bfs(i,j):
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[i][j] = True
    que = deque([[i,j,0]])

    res = 0
    while que:
        y,x,d = que.popleft()

        for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0 <= y+dy < H and 0 <= x+dx < W and S[y+dy][x+dx] == "." and not visited[y+dy][x+dx]:
                que.append([y+dy,x+dx,d+1])
                visited[y+dy][x+dx] = True
                res = max(res,d+1)

    return res

res = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            d = bfs(i,j)
            res = max(res,d)

print(res)
