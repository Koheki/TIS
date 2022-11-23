N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

His = ["" for _ in range(N)]

Score = {'r':R,'s':S,'p':P}
def hand(t):
    if t == 'r':
        return 'p'
    elif t == 's':
        return 'r'
    else:
        return 's'

res = 0
for i in range(N):
    t = T[i]
    w = hand(t)
    if i < K-1:
        res += Score[w]
        His[i] = w
    else:
        if His[i-K] == w:
            His[i] = 'x'
        else:
            res += Score[w]
            His[i] = w

print(res)
