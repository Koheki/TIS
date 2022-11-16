H,W,K = map(int,input().split())
C = [ [c for c in input()] for _ in range(H)]
res = 0

for h in range(1<<H):
    for w in range(1<<W):
        s = 0
        for i in range(H):
            for j in range(W):
                if (h>>i)&1 == 0 and (w>>j)&1 == 0 and C[i][j] == "#":
                    s += 1
        if s == K: res += 1

print(res)

