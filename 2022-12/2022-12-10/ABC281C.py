N,T = map(int,input().split())
A = [int(n) for n in input().split()]

T %= sum(A)

for i in range(N):
    if T - A[i] < 0:
        print(i+1,T)
        break
    T -= A[i]