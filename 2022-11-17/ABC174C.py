K = int(input())

if K % 2 == 0:
    print(-1)
    exit()

m = set()
N = 7

for i in range(1,K+1):
    N %= K
    if N == 0:
        print(i)
        exit()

    if N in m:
        print(-1)
        exit()
    
    m.add(N)
    N *= 10
    N += 7

print(-1)