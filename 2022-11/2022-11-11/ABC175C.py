X,K,D = map(int,input().split())

X = abs(X)
if K <= X//D:
    print(X-(D*K))
else:
    N = K - X//D
    if N %2 == 0:
        print(X%D)
    else:
        print(abs(X%D-D))