N = int(input())
xy = [[int(n) for n in input().split()] for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            x1,y1 = xy[i]
            x2,y2 = xy[j]
            x3,y3 = xy[k]

            if x1 != x2:
                y = ((y2-y1)/(x2-x1))*(x3-x1)+y1
                if y == y3:
                    print("Yes")
                    exit()
            else:
                if x1 == x3:
                    print("Yes")
                    exit()
print("No")
