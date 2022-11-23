from collections import deque

S = deque([ s for s in input()])
Q = int(input())

rev = False
for _ in range(Q):
    T = [s for s in input().split()]

    if len(T) == 1:
        rev = False if rev else True
    else:
        F,C = T[1],T[2]
        if rev:
            if F == "1":
                S.append(C)
            else:
                S.appendleft(C)
        else:
            if F == "1":
                S.appendleft(C)
            else:
                S.append(C)

if rev:
    S = reversed(S)

print("".join(S))
