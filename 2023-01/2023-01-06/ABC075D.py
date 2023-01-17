N,K = map(int,input().split())
XY = [[int(n) for n in input().split()] for _ in range(N)]

res = float("INF")

for i in range(N):
    for j in range(i+1,N):
        for k in range(N):
            for n in range(k+1,N):                
                top = max([XY[i][1],XY[j][1],XY[k][1],XY[n][1]])
                bottom = min([XY[i][1],XY[j][1],XY[k][1],XY[n][1]])
                left = min([XY[i][0],XY[j][0],XY[k][0],XY[n][0]])
                right = max([XY[i][0],XY[j][0],XY[k][0],XY[n][0]])

                c = 0
                for m in range(N):
                    if bottom <= XY[m][1] <= top and left <= XY[m][0] <= right:
                        c += 1

                if K <= c:
                    res = min(res,(top-bottom)*(right-left))

print(res)