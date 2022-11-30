N,K = map(int,input().split())
A = [int(n) for n in input().split()]

res = [0 for _ in range(N)]

if K < N:
    for i in range(K,N):
        res[i-K] = A[i]

print(*res)