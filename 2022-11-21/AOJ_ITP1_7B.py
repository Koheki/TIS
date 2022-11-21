while 1:
    n,x = map(int,input().split())

    if n == 0 and x == 0:
        exit()

    res = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            m = x - (i+j)
            if j < m <= n:
                res += 1
    print(res)
