N,T = map(int,input().split())
A = list(map(int,input().split()))

T %= sum(A)

for i in range(N):
    if T - A[i] < 0:
        print(i+1,T)
        exit()
    T -= A[i]