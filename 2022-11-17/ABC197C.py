N = int(input())
A = [int(n) for n in input().split()]

res = float("inf")

for i in range(1<<(N-1)):
    l = []
    n = A[0]
    for j in range(N-1):
        if (i>>j)&1:
            l.append(n)
            n = A[j+1]
        else:
            n |= A[j+1]

    l.append(n)
    n = l[0]
    for k in range(1,len(l)):
        n ^= l[k]
    res = min(res,n)

print(res)