N,M = map(int,input().split())
A = [int(n) for n in input().split()]

sums = [0]*(N+1)
for i in range(1,N+1):
    sums[i] = sums[i-1]+A[i-1]

res = 0
score = 0

for i in range(M):
    score += A[i]*(i+1)
res = score

for j in range(M,N):
    i = j-M
    score -= (sums[j]-sums[i])
    score += A[j]*M
    res = max(res,score)

print(res)


