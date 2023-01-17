N,A,B = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

GCD = gcd(A,B)
LCD = (A*B)//GCD
a,b,d = (N//A),(N//B),(N//LCD)

print(N*(N+1)//2 -(a*(a+1)//2)*A - ((b*(b+1))//2)*B + ((d*(d+1))//2)*LCD)

