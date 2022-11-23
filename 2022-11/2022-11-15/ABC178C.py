N = int(input())
mod = 10**9+7

res,n,o = 1,1,1

for _ in range(N):
    res *= 10
    n *= 9
    o *= 8

    res %= mod
    n %= mod
    o %= mod

res -= 2*n
res %= mod
res += o
res %= mod

print(res)

