N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]

res = 0

for i in range(N):
    score = C
    for j in range(M):
        score += (A[i][j]*B[j])
    if score > 0:
        res += 1

print(res)
