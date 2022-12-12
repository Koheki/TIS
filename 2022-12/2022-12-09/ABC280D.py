K = int(input())

k = K
res = 1
N = int(k**0.5)
for i in range(2,N+1):
    if k % i == 0:
        e = 0
        while k%i == 0:
            e += 1
            k //= i
        n = 0
        while e > 0:
            n += i
            x = n
            while x%i==0:
                x //= i
                e -= 1
        res = max(res,n)

res = max(res,k)
print(res)




