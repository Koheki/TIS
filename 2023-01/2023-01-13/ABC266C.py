Points = [[int(n) for n in input().split()] for _ in range(4)]

def cross(x1,y1,x2,y2):
    return x1*y2-x2*y1

flag = True
for i in range(4):
    a = Points[i%4]
    b = Points[(i+1)%4]
    c = Points[(i+2)%4]

    vec_ab = [b[0]-a[0],b[1]-a[1]]
    vec_bc = [c[0]-b[0],c[1]-b[1]]

    if cross(*vec_ab,*vec_bc) < 0:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
