import itertools

N,K = map(int,input().split())
T = [[int(n) for n in input().split()] for _ in range(N)]

path = itertools.permutations([i for i in range(1,N)])

res = 0
for p in path:
    cost = 0
    s = 0
    for g in p:
        cost += T[s][g]
        s = g
    cost += T[s][0]
    
    if cost == K:
        res += 1

print(res)

