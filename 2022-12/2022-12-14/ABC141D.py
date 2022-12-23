import heapq

N,M = map(int,input().split())
A = [-int(n) for n in input().split()]

heapq.heapify(A)

for _ in range(M):
    n = -heapq.heappop(A)
    heapq.heappush(A,-(n//2))

print(-sum(A))