N,K = map(str,input().split())
K = int(K)

for _ in range(K):
    n1 = int("".join(sorted(N,reverse=True)))
    n2 = int("".join(sorted(N)))
    N = str(n1-n2)

print(N)