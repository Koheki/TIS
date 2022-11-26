H,M = map(int,input().split())

for i in range(23):
    for m in range(M,60):
        h = (H+i)%24
        if h%10 < 6 and m//10 < 4:
            print(h,m)
            exit()

        if m == 59:
            M = 0

