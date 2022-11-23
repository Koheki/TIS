N = int(input())
S = [ s for s in input()]
Q = int(input())
rev = False

for _ in range(Q):
    t,a,b = map(int,input().split())
    a -= 1
    b -= 1

    if t == 1:
        if rev:
            a = a + N if a < N else a - N
            b = b + N if b < N else b - N
        S[a],S[b] = S[b],S[a]

    else:
        rev = False if rev else True

if rev == False:
    S = "".join(S)
else:
    S = "".join(S[N:]+S[:N])

print(S)