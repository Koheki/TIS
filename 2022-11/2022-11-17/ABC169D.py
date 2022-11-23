N = int(input())

def prime_factorize(n):
	res = []
	for i in range(2,int(n**0.5)+1):
		if n % i != 0:
			continue
		e = 0
		while n % i == 0:
			e += 1
			n //= i

		res.append((i,e))

	if n != 1:
		res.append((n,1))
	
	return res

res = 0
Prime = prime_factorize(N)

for i,c in Prime:
    n = 1
    while n <= c:
        res += 1
        c -= n
        n += 1

print(res)
