N = int(input())*2
div = []

for i in range(1,int(N**0.5)+1):
    if N % i != 0: continue

    div.append(i)
    if N//i != i:
        div.append(N//i)

res = 0
for d in div:
    if (d%2) == ((N//d)%2):
        continue
    res += 1

print(res)
