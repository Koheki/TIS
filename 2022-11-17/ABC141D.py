import heapq

N,M = map(int,input().split())
A = [int(n)*(-1) for n in input().split()]

heapq.heapify(A)

for _ in range(M):
    x = heapq.heappop(A)
    x = -x//2
    heapq.heappush(A,-x)

print(sum(A)*(-1))
