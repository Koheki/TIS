N  = int(input())

res = []

for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        res.append(i)
        if N%i == i:
            continue
        res.append(N//i)

res.sort()

for a in res:
    print(a)