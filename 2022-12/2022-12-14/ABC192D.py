X = input()
M = int(input())

def convn(x,n):
    c = 1
    res = 0
    while x > 0:
        res += (x%n)*c
        x //= n
        c *= n
    return res

n = 0
for i in [str(n) for n in range(9,-1,-1)]:
    if i in X:
        n = int(i)
        break

X = int(X)

l,r = 0,M
while r-l > 1:
    m = l+(r-l)//2

    a = conv