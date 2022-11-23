N,K = map(int,input().split())
P = [int(n) for n in input().split()]

E = [0 for _ in range(N)]
E[0] = (P[0]+1)/2

for i in range(1,N):
    p = P[i]
    E[i] = E[i-1] + (p+1)/2

res = E[K-1]

for i in range(K,N):
    j = i-K
    e = E[i] - E[j]
    res = max(res,e)

print(res)
