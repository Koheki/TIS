H,W = map(int,input().split())

if H == 1 or W == 1:
    print(1)
    exit()

res = (H//2)*W

if H %2:
    res += (W//2 + W%2)

print(res)
