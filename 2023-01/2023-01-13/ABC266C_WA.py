import math

ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
dx,dy = map(int,input().split())

def checker(x1,y1,x2,y2,x3,y3):
    A = (x2-x1,y2-y1)
    B = (x3-x1,y3-y1)

    cosT = (A[0]*B[0]+A[1]*B[1])/(math.sqrt(A[0]**2+A[1]**2)*math.sqrt(B[0]**2+B[1]**2))

    if cosT >= 0:
        return True
    return False

if checker(ax,ay,bx,by,dx,dy) and checker(bx,by,ax,ay,cx,cy) and checker(cx,cy,bx,by,dx,dy) and checker(dx,dy,cx,cy,ax,ay):
    print("Yes")
else:
    print("No")
