N = int(input())
S = [int(n) for n in input().split()]

A = [0]*N
A[0] = S[0]
sumA = S[0]

for i in range(1,N):
    A[i] = S[i] - sumA
    sumA += A[i]

print(*A)
