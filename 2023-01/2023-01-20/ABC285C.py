S = input()

res = 0
for s in S:
    res = res*26 + (ord(s)-ord('A')+1)

print(res)
