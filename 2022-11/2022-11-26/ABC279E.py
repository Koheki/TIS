from collections import deque

N,M = map(int,input().split())
A = [int(n) for n in input().split()]

B = [i for i in range(N+1)]

res = [0 for _ in range(M)]
que = deque([1])

while que:
    j = que.popleft()



