H,W = map(int,input().split())

dist = [[s for s in input()] for _ in range(H)]
sx,sy = -1,-1

for i in range(H):
    if "S" in dist[i]:
        sx = dist[i].index("S")
        sy = i
        break

stack = [[sy,sx,0]]
visited = [[False for _ in range(W)] for _ in range(H)]

while stack:
    y,x,d = stack.pop()
    visited[y][x] = True
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= y+dy < H and 0 <= x+dx < W:
            if y+dy == sy and x+dx == sx and d >= 3:
                print("Yes")
                exit()
            if dist[y+dy][x+dx] == "." and visited[y+dy][x+dx] == False:
                stack.append([y+dy,x+dx,d+1])
print("No")
