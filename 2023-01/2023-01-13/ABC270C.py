from collections import defaultdict,deque

N,X,Y = map(int,input().split())
Tree = defaultdict(list)

for _ in range(N-1):
    U,V = map(int,input().split())
    Tree[U].append(V)
    Tree[V].append(U)

que = deque([X])
path = [None]*(N+1)
path[X] = 0

while que:
    node = que.popleft()
    if node == Y:
        break
    for v in Tree[node]:
        if path[v] == None:
            que.append(v)
            path[v] = node

res = [Y]
node = Y
while node != X:
    res.append(path[node])
    node = path[node]
res.reverse()
print(*res)
