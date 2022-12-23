
N = int(input())
X = list(map(int,input().split()))

res = float("INF")

for i in range(min(X),max(X)+1):
    p = 0
    for j in range(N):
        p += (X[j] -i)**2

    res = min(res,p)

print(res)

