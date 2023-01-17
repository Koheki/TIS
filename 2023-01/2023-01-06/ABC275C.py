import collections

N = int(input())
A = [int(n) for n in input().split()]

countA = collections.Counter(A)
sumA = {k:0 for k in range(N)}

A.sort()
types = len(set(A))-1
c = 0
for i in range(N):
    if i+1 <N and A[i] != A[i+1]:
        sumA[types] = i+1 - c
        types -= 1
        c = i+1
sumA[types] = N -c

for i in range(N):
    print(sumA[i])
