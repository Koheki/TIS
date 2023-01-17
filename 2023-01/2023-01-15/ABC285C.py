S = input()
res = 0
for s in S:
    res = res*26 + (ord(s)-64)

print(res)