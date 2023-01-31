N,A,B = map(int,input().split())
S = [s for s in input()]

res = float("INF")
for i in range(N//2):
    c = 0
    for j in range(N//2):
        q = (N-j+i-1)%N
        p = (i+j)%N 
        if S[p] != S[q]:
            c += 1
    res = min(res,A*(i)+B*(c))
print(res)