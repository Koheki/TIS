N,K = map(int,input().split())
A = [int(n) for n in input().split()]

visited = [False for _ in range(N)]
cur = 0
cyc = []

while not visited[cur]:
    visited[cur] = True
    cyc.append(cur+1)
    cur = A[cur]-1

h = 0
k = len(cyc)
for i in range(len(cyc)):
    if cyc[i] == (cur+1):
        break
    h += 1
    k -= 1

if K < h:
    print(cyc[K])
else:
    n = (K-h)%k
    print(cyc[h+n])