N,P,Q,R,S = map(int,input().split())
A = [int(n) for n in input().split()]

X = Q-P
P -= 1
R -= 1
for i in range(X+1):
    A[P+i],A[R+i] = A[R+i],A[P+i]

print(*A)
