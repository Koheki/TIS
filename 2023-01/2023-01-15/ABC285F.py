from collections import Counter

N = int(input())
S = [s for s in input()]

mat = [[0]*26 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(26):
        mat[i][j] = mat[i-1][j]
    n = ord(S[i-1])-97
    mat[i][n] += 1

Q = int(input())

for _ in range(Q):
    query = [q for q in input()]

    if query[0] == '1':
        x = int

    else:
