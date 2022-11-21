N = int(input())
A = [int(n) for n in input().split()]

# pairwise
pairwise = True
n = max(A)
prime = [True for _ in range(n+1)]
prime[0],prime[1] = False,False
D = [1 for _ in range(n+1)]

for i in range(2,n+1):
    if prime[i]:
        D[i] = i
        c = 2*i
        while c <= n:
            prime[c] = False
            D[c] = i
            c += i

checker = set()
for i in range(N):
    a = A[i]
    while a != 1:
        d = D[a]
        if d in checker:
            pairwise = False
            break
        checker.add(d)
        while a%d == 0:
            a//=d
    if not pairwise:
        break

if pairwise:
    print("pairwise coprime")
    exit()

# setwise
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

setwise = A[0]
for i in range(1,N):
    setwise = gcd(setwise,A[i])

if setwise == 1:
    print("setwise coprime")
else:
    print("not coprime")
