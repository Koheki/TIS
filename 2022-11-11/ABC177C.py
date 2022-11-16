N = int(input())
mod = 10**9+7
A = [int(n)%mod for n in input().split()]
S = [0 for _ in range(N)]
S[0] = A[0]
for i  in range(1,N):
    S[i] = (A[i]+S[i-1])%mod

res = 0
for i in range(N):
    res += (A[i]*(S[N-1] - S[i]))%mod
    res %= mod

print(res)
