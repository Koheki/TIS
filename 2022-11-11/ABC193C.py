N = int(input())

prime = set()

ex = 0
for i in range(2,int(N**0.5)+1):
    c = i**2
    if c not in prime:
        while c <= N:
            ex += 1
            prime.add(c)
            c *= i

print(N-ex)
