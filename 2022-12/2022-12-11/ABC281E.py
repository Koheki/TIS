import heapq

N,M,K = map(int,input().split())
A = [int(n) for n in input().split()]

sortedA = sorted(zip(A[:M],range(M)))

s = 0
is_sumed = [False]*N
L = []

for a, i in sortedA[:K]:
    is_sumed[i] = True
    s += a
    heapq.heappush(L,(-a,i))

R = []
for i in range(K,M):
    heapq.heappush(R,sortedA[i])

res = [s]
for i in range(M,N):
    a = A[i]
    heapq.heappush(R,(a,i))

    if is_sumed[i-M]:
        is_sumed[i-M] = False
        s -= A[i-M]
        add_a, add_i = heapq.heappop(R)
        while len(R) and add_i < i-M:
            add_a,add_i = heapq.heappop(R)
        s += add_a
        is_sumed[add_i] = True
        heapq.heappush(L,(-add_a,add_i))

    if M != K:
        pop_a, pop_i = heapq.heappop(L)
        while not is_sumed[pop_i]:
            pop_a,pop_i = heapq.heappop(L)

        add_a,add_i = heapq.heappop(R)
        while len(L) and add_i < i - M:
            add_a, add_i = heapq.heappop(R)

        if add_i >= i-M and -pop_a > add_a:
            s += pop_a
            is_sumed[pop_i] = False
            heapq.heappush(R,(-pop_a,pop_i))
            s += add_a
            is_sumed[add_i] = True
            heapq.heappush(L,(-add_a,add_i))
        else:
            heapq.heappush(L,(pop_a,pop_i))
            heapq.heappush(R,(add_a,add_i))
    res.append(s)

print(*res)

