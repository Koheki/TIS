from collections import Counter

N,M = map(int,input().split())
A = [int(n) for n in input().split()]
total = sum(A)

A.sort()
s = 0
for i in range(1,N):
    if A[i] - A[i-1] > 1:
        s = i
        break

res = 0
tmp = 0
for i in range(N):
    cur = (s+i)%N
    tmp += A[cur]
    if (A[(cur+1)%N] - A[cur])%M > 1:
        res = max(res,tmp)
        tmp = 0

res = max(res,tmp)
print(total-res)
