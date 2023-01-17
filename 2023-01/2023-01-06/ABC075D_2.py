N,K = map(int,input().split())
XY = [[int(n) for n in input().split()] for _ in range(N)]

res = float("INF")

for x1 in range(N):
    for x2 in range(x1+1,N):
        for y1 in range(N):
            for y2 in range(y1+1,N):
                top = max(XY[y1][1],XY[y2][1])
                bottom = min(XY[y1][1],XY[y2][1])
                left = min(XY[x1][0],XY[x2][0])
                right = max(XY[x1][0],XY[x2][0])

                c = 0
                for m in range(N):
                    if bottom <= XY[m][1] <= top and left <= XY[m][0] <= right:
                        c += 1

                if K <= c:
                    res = min(res,(top-bottom)*(right-left))

print(res)