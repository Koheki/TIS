N = int(input())
A = input()
B = input()

mod =998244353

m = []
M = []

for a,b in zip(A,B):
    if b < a:
        a,b, = b,a

    m.append(a)
    M.append(b)

A = int(''.join(m))
B = int(''.join(M))

print((A*B)%mod)
