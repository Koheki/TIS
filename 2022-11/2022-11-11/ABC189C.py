N = int(input())
A = [int(n) for n in input().split()]

res = 0
for i in range(N):
    x = A[i]
    for j in range(i,N):
        x = min(x,A[j])
        res = max(res,x*(j-i+1))
print(res)