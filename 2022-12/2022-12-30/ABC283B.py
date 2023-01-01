N = int(input())
A = [int(n) for n in input().split()]
Q = int(input())

for _ in range(Q):
    q = [int(n) for n in input().split()]

    if q[0] == 1:
        A[q[1]-1] = q[2]
    else:
        print(A[q[1]-1])
