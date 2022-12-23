A,B = map(int,input().split())

socket = 1
res = 0
while socket < B:
    res += 1
    socket += (A-1)

print(res)