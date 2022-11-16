import math

N = int(input())
A = [int(n) for n in input().split()]

div2 = [0 for _ in range(N)]
div3 = [0 for _ in range(N)]

for i in range(N):
    if A[i] % 2 == 0:
        while A[i] % 2 == 0:
            A[i] //= 2
            div2[i] += 1
    
    if A[i] % 3 == 0:
        while A[i] % 3 == 0:
            A[i] //= 3
            div3[i] += 1

flag = True
for i in range(N-1):
    if A[i] != A[i+1]:
        flag = False
        break

if flag == False:
    print(-1)
else:
    res = sum(div2) - min(div2)*N
    res += sum(div3) - min(div3)*N
    print(res)
