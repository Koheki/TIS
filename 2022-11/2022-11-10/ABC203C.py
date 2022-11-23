N,K = map(int,input().split())

town = [[int(n) for n in input().split()] for _ in range(N)]

town.sort()

for i in range(N):
    a,b = town[i]

    if a > K:
        break
    K += b

print(K)
