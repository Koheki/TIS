N = int(input())
S = set()
flag = True

for _ in range(N):
    s = input()

    if s[0] not in ['H','D','C','S']:
        flag = False
        break
    
    if s[1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        flag = False
        break

    if s in S:
        flag = False
        break

    S.add(s)

if flag:
    print("Yes")
else:
    print("No")