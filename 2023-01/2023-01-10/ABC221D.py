from collections import defaultdict

N = int(input())
X = defaultdict(int)
for _ in range(N):
    a,b = map(int,input().split())
    X[a] += 1
    X[a+b] -= 1

D = [0]*(N+1)

user = 0
A = sorted(X.keys())

for i in range(len(A)-1):
    user += X[A[i]]
    D[user] += (A[i+1]-A[i])

print(*D[1:])