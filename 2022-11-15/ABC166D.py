X = int(input())

for a in range(-118,200):
    for b in range(-118,200):
        if a**5 - b**5 == X:
            print(a,b)
            exit()

# https://img.atcoder.jp/abc166/editorial.pdf

"""
- concise
- procedure
- convey

"""