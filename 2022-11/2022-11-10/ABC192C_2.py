N,K = map(str,input().split())
K = int(K)

for _ in range(K):
    n1 = "".join(sorted(N,reverse=True))
    n2 = "".join(sorted(N))

    n = len(n1)
    s = 0
    for i in range(n):
        j = n - i - 1
        s += (int(n1[j])-int(n2[j]))*10**i
    N = str(s)

print(N)