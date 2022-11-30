H,W = map(int,input().split())

S = [[s for s in input()] for _ in range(H)]
T = [[s for s in input()] for _ in range(H)]

for i in range(H):
    if S[i].count('#') != T[i].count('#'):
        print("No")
        exit()

print("Yes")
