A,B,X = map(int,input().split())

def d(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

l = 0
r = 10**9+1

while r -l > 1:
    m = l + (r-l)//2
    n = A*m + B*d(m)
    
    if n <= X:
        l = m
    else:
        r = m

print(l)
