
N,Q = map(int,input().split())

FF = set()
for _ in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        FF.add((a,b))
    elif t == 2:
        FF.discard((a,b))
    else:
        if (a,b) in FF and (b,a) in FF:
            print("Yes")
        else:
            print("No")