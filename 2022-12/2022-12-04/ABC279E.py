N,M = map(int,input().split())
A = [int(n)-1 for n in input().split()]
S = [-1]*M
p = 0

for i in range(M):
    S[i] = p
    if A[i] == p:
        p += 1
    elif A[i]+1 == p:
        p -= 1

L = list(range(N))

ans = []
for i in range(M-1,-1,-1):
    ans.append(L[S[i]]+1)

    L[A[i]],L[A[i]+1] = L[A[i]+1],L[A[i]]

print(*ans[::-1],sep="\n")
