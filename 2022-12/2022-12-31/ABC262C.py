N = int(input())
A = [int(n)-1 for n in input().split()]

ij,ji = 0,0

for i in range(N):
    if A[i] == i:
        ij += 1
    elif A[A[i]] == i:
        ji += 1

print(ij*(ij-1)//2+ji//2)