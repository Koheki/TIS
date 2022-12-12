N,P = map(int,input().split())
mod = 998244353

dp = [0]*(N+2)
b = pow(100,mod-2,mod)

p2 = (P*b)%mod
p1 = ((100-P)*b)%mod

for i in range(N-1,-1,-1):
    dp[i] += ((dp[i+1]+1)*p1)%mod 
    dp[i] += ((dp[i+2]+1)*p2)%mod
    dp[i] %= mod

print(dp[0])
