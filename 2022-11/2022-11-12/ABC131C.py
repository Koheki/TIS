A,B,C,D = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

CD = (C*D)//gcd(C,D)

def countdiv(X,Y):
    c = 0
    while X > 0:
        X //= Y
        c += 1
    return c

Adiv = A - 1 - (countdiv(A-1,C) + countdiv(A-1,D) - countdiv(A-1,CD))
Bdiv = B - (countdiv(B,C) + countdiv(B,D) - countdiv(B,CD))

print(Bdiv- Adiv)
