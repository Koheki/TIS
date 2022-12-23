a,b = map(str,input().split())

N = int(a+b)**0.5

if N//1 == N:
    print("Yes")
else:
    print("No")
