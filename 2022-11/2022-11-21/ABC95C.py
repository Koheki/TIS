A,B,C,X,Y = map(int,input().split())

N = max(X,Y)
res = float("inf")
for i in range(N+1):
    nx,ny = max(X-i,0),max(Y-i,0)
    p = A*nx + B*ny + C*(2*i)
    res = min(res,p)
print(res)