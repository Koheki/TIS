N = int(input())

res = 0
for n in range(3,N+1)[::2]:
    p = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            x = 0
            while n%i==0:
                n//=i
                x += 1
            p *= (x+1)
    
    if n != 1:
        p *= 2

    if p == 8:
        res += 1

print(res)
