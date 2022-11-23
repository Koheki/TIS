H,W,X,Y = map(int,input().split())
S = [[s for s in input()] for _ in range(H)]

X -= 1
Y -= 1
res = 0
tmp = 0

for h in range(H):
    if h <= X:
        tmp += 1
        if S[h][Y] == "#":
            tmp = 0
    else:
        if S[h][Y] == "#":
            break
        tmp += 1

res = tmp - 1
tmp = 0

for w in range(W):
    if w <= Y:
        tmp += 1
        if S[X][w] == "#":
            tmp=0
    else:
        if S[X][w] == "#":
            break
        tmp += 1

res += tmp
print(res)
