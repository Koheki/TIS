n,a,b = map(int,input().split())
mod = 10**9+7

def modpow(a,n):
    res = 1
    while n > 0:
        if n & 1:
            res *= a
            res %= mod
        a *= a
        a %= mod
        n >>= 1
    return res

def nCr(n,r):
    x = 1
    y = 1
    for i in range(r):
        x *= (n - i)
        x %= mod
    for j in range(2,r+1):
        y *= j
        y %= mod
    y = modpow(y,mod-2)
    return (x*y)%mod

res = modpow(2,n)
res -= nCr(n,a)
res -= nCr(n,b)

print(res%mod)