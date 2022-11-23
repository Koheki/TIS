N = int(input())
P = sorted([tuple([int(n) for n in input().split()]) for _ in range(N)])
setP = set(P)

res = 0
for i in range(N):
    for j in range(i+1,N):
        xi,yi = P[i]
        xj,yj = P[j]

        qx, qy = xj-yj+yi, yj+xj-xi
        rx, ry = xi-yj+yi, yi+xj-xi

        if (qx,qy) in setP and (rx,ry) in setP:
            res = max(res,(xi-xj)**2+(yi-yj)**2)

print(res)
