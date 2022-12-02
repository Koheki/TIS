
def transpose(A):
    m,n = len(A),len(A[0])

    tA = [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            tA[j][i] = A[i][j]
    return tA


H,W = map(int,input().split())

S = [[c for c in input()] for _ in range(H)]
T = [[c for c in input()] for _ in range(H)]


S = sorted(transpose(S))
T = sorted(transpose(T))

if S == T:
    print("Yes")
else:
    print("No")


