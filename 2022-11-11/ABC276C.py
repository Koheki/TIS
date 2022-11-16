N = int(input())
P = [int(n) for n in input().split()]

n = 0
for i in range(N-2):
    if P[i] > P[i+1] and P[i+1] < P[i+2]:
        n = i

Psub = P[n+1:]
p = P[n]

m = 0
for j in range(p-1,0,-1):
    if j in Psub:
        m = j
        break

i = Psub.index(m)

Q = [Psub[i]]
Psub[i] = p

Q.extend(sorted(Psub,reverse=True))

print(*(P[:n] + Q)) 

