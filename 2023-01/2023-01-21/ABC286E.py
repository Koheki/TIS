from collections import defaultdict, deque

N = int(input())
A = [int(n) for n in input().split()]

Graph = defaultdict(list)

for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == 'Y':
            Graph[i].append(j)

def solve(s,g):
    que = deque([[s,0,A[s]]])
    visited = set()
    visited.add(s)
    shortest = float("INF")
    res = 0
    while que:
        n,d,c = que.pop()
        if n == g:
            visited.discard(g)
            if d < shortest:
                res = c
                shortest = d
            elif d == shortest:
                res = max(res,c)
            else:
                continue
        else:
            for m in Graph[n]:
                if m not in visited:
                    visited.add(m)
                    que.append([m,d+1,c+A[m]])

    if shortest == float("INF"):
        return -1,False
    return shortest, res

Q = int(input())
for _ in range(Q):
    U,V = map(lambda x:int(x)-1,input().split())
    d,c = solve(U,V)

    if d < 0:
        print("Impossible")
    else:
        print(d,c)
