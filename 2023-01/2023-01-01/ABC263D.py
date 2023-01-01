N, L, R = map(int,input().split())
A = [int(n) for n in input().split()]

Rfill = [0]*N
Rfill[0] = min(A[-1],R)

