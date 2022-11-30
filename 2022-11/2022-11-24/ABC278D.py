N = int(input())
A = [int(n) for n in input().split()]
Q = int(input())

pair = {i:(A[i],0) for i in range(N)}

x = (0,0)
for j in range(Q):
    q = [int(n) for n in input().split()]

    if q[0] == 1:
        x = (q[1],j)

    elif q[0] == 2:
        i = q[1] - 1
        v,t = pair[i]

        if t < x[1]:
            pair[i] = (x[0]+q[2],j)
        else:
            pair[i] = (v+q[2],j)

    else:
        i = q[1] - 1
        if t < x[1]:
            print(x[0])
        else:
            print(pair[i][0])

