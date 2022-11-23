N = int(input())
P = sorted([tuple([int(n) for n in input().split()]) for _ in range(N)])

def bisearch(seq,target):
    l = 0
    r = len(seq)-1
    while l <= r:
        m = l + (r-l)//2
        if seq[m] == target:
            return True
        elif seq[m] < target:
            l = m + 1
        else:
            r = m-1
    return False
 
res = 0
for i in range(N):
    for j in range(i+1,N):
        xi,yi = P[i]
        xj,yj = P[j]

        qx, qy = xj-yj+yi, yj+xj-xi
        rx, ry = xi-yj+yi, yi+xj-xi

        if bisearch(P,(qx,qy))  and bisearch(P,(rx,ry)):
            res = max(res,(xi-xj)**2+(yi-yj)**2)

print(res)
